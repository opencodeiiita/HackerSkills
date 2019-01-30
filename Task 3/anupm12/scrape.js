var request = require('request');
var cheerio = require('cheerio');
var fs = require('fs');

request('https://inshorts.com/en/read/',(error,response, html) => {
    if(!error && response.statusCode == 200) {
        var $ = cheerio.load(html);
        var items = [];

        $('.news-card').each((i,el) => {
            var title = $(el)
            .find('.clickable') .text() .replace(/\s\s+/g, '');
            var content = $(el) .find('.news-card-content') .text();
            var cont = content.substring(5, content.length);
            var link = $(el) .find('.news-card-image') .attr('style');
            var url = link.substring(23, link.length-2);

            items.push({
                "Title: ": title , "Content: " : cont ,  "Link: " : url 
             });

             var myObj = {
                "data: " : items    
            };

            fs.writeFile("data.json",JSON.stringify(myObj, null, 4) , function(err) {
                if(err) 
                    return console.log(err);
             });
        });
        console.log('Scraping successfully done!!!');
    }
});