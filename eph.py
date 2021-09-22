import ephem

mars = ephem.Mars('2021/09/22')
const = ephem.constellation

print(const(mars))
