from pydantic import BaseModel, Field
from langchain_core.tools import BaseTool
from typing import Type

class InterestSchema(BaseModel):
    principal: int = Field(
        description="""The initial investment amount.
Example: 1000 for 1000 USD"""
    )
    interest_rate: float = Field(
        description="""The monthly interest rate as percentage. Pass just the number without '%' symbol.
Example: 3 for %3 monthly return."""
    )
    months: int = Field(
        description="""The time period in months for the investment.
Example: 12 for one year, 6 for six months."""
    )


class InterestTool(BaseTool):
    name: str = "CalculateInterest"
    description: str = """
Use this tool to calculate compound interest returns over a specified period.

Examples:
- Question: "What would $10000 become with 3% monthly interest after 12 months?
  Tool input: {"principal": 10000, "interest_rate": 3, "months": 12}
  
- Question: "What would $5000 become with 2.5% monthly interest after 9 months?
  Tool input: {"principal": 5000, "interest_rate": 2.5, "months": 9}
  
- Question: "What would $12.500 become with 11% monthly interest after a year and a half?
  Tool input: {"principal": 12500, "interest_rate": 11, "months": 18}

The tool will return the final amount after compound interest is applied.
All inputs should be numbers without any currency or percentage symbols (no $, %, etc.)
"""
    args_schema: Type[BaseModel] = InterestSchema
    verbose: bool = True

    def _run(self,
             principal: int,
             interest_rate: float,
             months: int
        ) -> float:
        return principal * (1 + interest_rate/100)**months