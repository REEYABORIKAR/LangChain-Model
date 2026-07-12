from langchain_text_splitters import RecursiveCharacterTextSplitter

text="""
All management employees on the roll of the Company shall be eligible for leave as detailed in this Policy.
Factory Workmen and PSRs are governed as per the respective settlement terms.
Contract/ Casual employees shall not be covered as per the terms of this Policy, they will be covered as per
the terms of their individual contracts.
For calculation of leave the calendar is considered from January 1 to December 31. If an employee joins the
organization any date after January 1, leave is calculated on a pro-rata basis from the date he/she joins till
December 31. Further, the following will be the terms for the eligibility for leave as per the terms of this
Policy.
In calculating the leave as per the terms of this Policy, fraction of leave of half a day or more shall be treated
as one full day's leave and fraction of less than half of the day shall be omitted.
"""

# Initialize the splitter
splitter=RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0
)

# Perform the split
chunks=splitter.split_text(text)
print(len(chunks))
print(chunks)

