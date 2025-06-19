from scrapes.goncalves import ScrapeGoncalves

scrape = ScrapeGoncalves()
data = scrape.consultaCarnes()

print('DADOS --> ', data)