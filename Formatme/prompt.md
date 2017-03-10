I am working with a system that gives me parameters based on some form data, but I need to rework all of the parameters in order to query my database!

For example, here is a parameter chain from one of my tasks:
`8F64-22B8-4198-8B63-28CF46AE58D5,Reprint,,,,,,, 11557, 11557,,,CI,I,E,RB,0,,,1,0,1,,1,0,0,0,0,0,1`

* For any empty slots in the parameter e.g. (`,,`) that are surrounded by commas must have NULL inserted into the index. For example --> `,,` becomes `,NULL,`
* For any indexes that contain solely numbers (which means no spaces) must be left alone.
 For example --> `,1,` remains `,1,`
* For any indexes that contain any combination of numbers, characters, symbols, and spaces must have single quotes added to the index. For example --> `,Reprint,` becomes `,'Reprint',`
* Additionally, the last parameter must be removed from every input. For example --> if my last two parameters were `...,0,1` it should be removed from my parameter chain completely resulting in --> `...,0`

Once my parameter chains are formatted, I can finally query my database! I do not want to hand write all of this out. OH and one last thing, make sure your input can take ANY length of input, some of these parameters are really lengthy! Others, not so much. Follow my rules above and you should be golden.

Note -- It is not necessary to create valid SQL here, but only to follow the formatting guidelines.


**Sample Input**
 `1ANV-23BA-BKLL-0764-2LL135KDA4C7,Reprint,,,,,,,=17067,=17067,,,HI,I,E,RB,0,,,1,0,1,,1,0,1,0,0,0,0`

**Sample Output**
`'1ANV-23BA-BKLL-0764-2LL135KDA4C7','Reprint',NULL,NULL,NULL,NULL,NULL,NULL,
'=17067','=17067',NULL,NULL,'HI','I','E','RB',0,NULL,NULL,1,0,1a,NULL,1,0,1,0,0,0`

**Sample Input**
`3XD2-34GB-PODA-9090-23SIZ5KBA668,Reprint,,,,,,,=81444,=81444,,,OP,D,B,RD,0,1,,1,0,,1,1,,1,,0,0,0`

**Sample Output**
`'3XD2-34GB-PODA-9090-23SIZ5KBA668','Reprint',NULL,NULL,NULL,NULL,NULL,NULL,
'=81444','=81444',NULL,NULL,'OP','D','B','RD',0,1,NULL,1,0,NULL,1,1,NULL,1,NULL,0,0`
