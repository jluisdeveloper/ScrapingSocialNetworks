require 'nokogiri'
require 'open-uri'
require 'pry'

url = "https://sci-hub.se"
queryPaper = "https://link.springer.com/article/10.1631/jzus.A0820320"  ## ACA PONES EL LINK DEL PAPER QUE QUIERE PIRATEAR

html = URI.open(url + "/" + queryPaper)

doc = Nokogiri::HTML(html)
url_download = ""

doc.search('#buttons').map do |element|
  url_download = element.children[1].attributes["onclick"].value  
end

url_download = url_download.split('\'', url_download.size)[1]
url_preview = url_download[..url_download.index("?download")-1]

puts url_download
puts url_preview