import wlog
import wscrap

wlog.set_custom_log_info('error.log')
news_scrap = wscrap.NewsScraper(wscrap.url_link, wlog)

## UNCOMMENT THE FOLLOWING 2 LINES OF CODE TO GET SITE'S LATEST DATA
## OTHERWISE THIS PROGRAM PARSE DATA FROM DISK FILE RETRIEVED PREVIOUSLY

# news_scrap.retrieve_webpage()
# news_scrap.write_webpage_as_html()

news_scrap.read_webpage_from_html()
news_scrap.convert_data_to_bs4()
news_scrap.parse_soup_to_simple_html()
