let axios = require('axios');
let cheerio = require('cheerio');
let fs = require('fs'); 
axios.get('https://inshorts.com/en/read/')
    .then((response) => {
        if(response.status === 200) {
            const html = response.data;
            const $ = cheerio.load(html); 
            let devtoList = [];
            $('.news-card').each(function(i, elem) {
                devtoList[i] = {
                    title: $(this).find('.news-card-title').text().trim(),
                    content: $(this).find('.news-card-content').text().trim(),
                    
                    imgurl: $(this).find('.news-card-image').attr('style')

                }      
            });
            const devtoListTrimmed = devtoList.filter(n => n != undefined )
            fs.writeFile('devtoList.json', 
                          JSON.stringify(devtoListTrimmed, null, 4), 
                          (err)=> console.log('File successfully written!'))
    }
}, (error) => console.log(err) );
