
data = {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}

#print(data)

#Standard Generalized Markup Language
print(data['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossTerm'])


# XML
print(data['glossary']['GlossDiv']['GlossList']['GlossEntry']['GlossDef']['GlossSeeAlso'][1])



#
# https://codeshare.io/adpYLR