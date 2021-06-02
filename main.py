from selenium import webdriver


titleClass = "h1"
titleName = "_2IIDsE _3I-nQy"
ratingClass = "span"
ratingName = "FDDgZI"
synopsisClass = "div"
synopsisName = "_3qsVvm _1wxob_"

storeFrontURL = "https://www.amazon.com/gp/video/storefront"
vidDownloadURL = "/gp/video/detail"


driver = webdriver.Chrome(executable_path="chromedriver")
driver.get(storeFrontURL)
