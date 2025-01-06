from pydantic import BaseModel, Field
from langchain_core.tools import BaseTool
from typing import Type
import yfinance as yf
from datetime import datetime
CURRENT_YEAR = datetime.now().year

class MetalPriceSchema(BaseModel):
    metal: str = Field(
        description="""The type of precious or industrial metal to analyze.
Common precious metals:
- 'gold' (Gold - GC=F)
- 'silver' (Silver - SI=F)
- 'platinum' (Platinum - PL=F)
- 'palladium' (Palladium - PA=F)

Example: 'platinum' for Platinum pricing.
Example: 'gold' for Gold pricing.

Note: Input just the metal name in lowercase, without symbols or additional words"""
    )
    year: int = Field(
        description=f"""The year to analyze metal performance.
Example: 2023 for year 2023
Must be between 1990 and current {CURRENT_YEAR}"""
    )

class MetalProfitTool(BaseTool):
    name: str = "CalculateMetalProfit"
    description: str = """
Use this tool to calculate the yearly profit/loss percentage of various metals including both precious and industrial metals.
The tool will return the yearly profit/loss percentage and price data for the specified metal.

Examples:
- Question: "How profitable was platinum in 2023?"
- Tool input: {"metal": "platinum", "year": 2023}

- Question: "What was gold's return in 2021?"
- Tool input: {"metal": "gold", "year": 2021}

- Question: "Compare the performance of 'silver' and 'gold' in 2022."
- First Tool input: {"metal": "silver", "year": 2022}
- Second Tool input {"metal": "gold", "year": 2022}
Then compare the results"""
    args_schema: Type[BaseModel] = MetalPriceSchema
    verbose: bool = True

    def get_symbol(self, metal: str) -> str:
        tickers = {
            "gold":"GC=F",
            "silver": "SI=F",
            "platinum": "PL=F",
            "palladium": "PA=F",
            "copper": "HG=F",
            "aluminum": "ALI=F",
            "zinc": "ZNC=F",
            "nickel": "NIC=F"
        }
        ticker = tickers.get(metal.lower())
        if ticker is None:
            raise ValueError(f"Can't get the ticker for {metal}!\n"+
                f"Supports only {', '.join(tickers.keys())}")    
        return ticker
    
    def _run(self, metal: str, year: int):
        try:
            if not 1990 <= year <= CURRENT_YEAR:
                return f"Error: Year must be between 1990 and {CURRENT_YEAR}, but got {year}!"
            start_date = datetime(year, 1, 1)
            end_date = datetime(year, 12, 31)
            
            ticker = self.get_symbol(metal)
            
            data = yf.download(ticker,
                               start=start_date.strftime("%Y-%m-%d"),
                               end=end_date.strftime("%Y-%m-%d"))
            year_data = data[data.index.year == year]
            if year_data.empty:
                return f"No data available for {metal} in {year}"
            
            first_price = float(year_data["Close"].iloc[0])
            last_price = float(year_data["Close"].iloc[-1])
            yearly_return = last_price - first_price

            highest_price = float(year_data["Close"].max())
            lowest_price = float(year_data["Close"].min())
            average_price = float(year_data["Close"].mean())
            
            return f"""Analysis for {metal.upper()} in {year}:
Performance Metrics:
* Starting Price: {first_price:.2f}
* Ending Price: {last_price:.2f}
* Total Return: {yearly_return:.2f}

Price Range:
* Highest: {highest_price:.2f}
* Lowest: {lowest_price:.2f}
* Average: {average_price:.2f}

Note: All prices are in USD."""
        except Exception as e:
            return f"""Error analyzing {metal} for {year}!\nError: {e}"""