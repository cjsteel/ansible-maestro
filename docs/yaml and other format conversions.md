### Converting json output

Once you dump your target hosts facts files you may want to use these as is or make them more human readable.

#### other conversion tools

* [json2html](http://json2html.herokuapp.com/)
* [html2markdown](http://www.codefu.org/html2markdown/)

#### json2md

* requires npm i json2md
* [json2md](https://github.com/IonicaBizau/json2md)
* [How to convert JSON to Markdown using json2md](http://ionicabizau.net/blog/27-how-to-convert-json-to-markdown-using-json2md)

#### http://pandoc.org/

Conversion using pandoc, html to md?

* http://pandoc.org/demos.html

Converting html to markdown:

        pandoc -s -r html maestro.html -o maestro.md
        pandoc -s -r html http://www.gnu.org/software/make/ -o example12.text

* Redmine default format: **Textile**

