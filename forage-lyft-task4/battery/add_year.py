def addYear(originalDate, year_add):
    result = originalDate.replace(year=originalDate.year + year_add)
    return result