## Exercise about matrix


#print all data with name less three caracters

countries = [['Egypt', ['USA', 'AR'], 'India'], ['Dubai', 'America', 'Spain'], ['London', 'England', 'France','BR']]
countries2  = [country for sublist in countries for country in sublist if len(country) < 4]
print(countries2)