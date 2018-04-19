[![Software License](https://img.shields.io/badge/License-MIT-orange.svg?style=flat-square)](https://github.com/entrepreneur-interet-general/open_api_schemas_to_markdown/blob/master/LICENSE.md)
![CircleCI](https://img.shields.io/circleci/project/github/entrepreneur-interet-general/open_api_schemas_to_markdown.svg?style=flat-square)
![PyPI](https://img.shields.io/pypi/open_api_schemas_to_markdown.svg?style=flat-square)


# OpenAPI Components Schemas to Markdown
The goal of this package is to generate [Github Flavored Markdown](https://github.github.com/gfm/) documentation of Components Schemas from the [OpenAPI 3 specification](https://github.com/OAI/OpenAPI-Specification).

Say you've got a YAML file:
```yml
openapi: "3.0.0"
info:
  version: "0"
  title: Demo
paths:
  /demo:
    get:
      summary: Demo
      responses:
        '200':
          description: OK
components:
  schemas:
    ResultatHumain:
      properties:
        operation_id:
          type: integer
          format: int64
          description: Le numéro unique de l'opération
          example: 1119920371
        categorie_personne:
          type: string
          description: Indique la catégorie de personne impliquée dans le bilan humain
          example: Pêcheur français
        resultat_humain:
          type: string
          description: Description du bilan humain
          example: Personne secourue
        nombre:
          type: number
          format: int32
          minimum: 0
          description: Nombre de personnes impliquées dans ce bilan
          example: 3
        dont_nombre_blesse:
          type: number
          format: int32
          minimum: 0
          description: Indique le nombre de personnes blessées dans le bilan
          example: 1

```

The package will produce a Markdown file from the YAML specification file with the following content:
```markdown
## ResultatHumain Model
|Field|Type|Description|Example|Properties|
|---|---|---|---|---|
|operation_id|integer($int64)|Le numéro unique de l'opération|1119920371||
|categorie_personne|string|Indique la catégorie de personne impliquée dans le bilan humain|Pêcheur français||
|resultat_humain|string|Description du bilan humain|Personne secourue||
|nombre|number($int32)|Nombre de personnes impliquées dans ce bilan|3|minimum: 0|
|dont_nombre_blesse|number($int32)|Indique le nombre de personnes blessées dans le bilan|1|minimum: 0|
```

And if you render it:
## ResultatHumain Model
|Field|Type|Description|Example|Properties|
|---|---|---|---|---|
|operation_id|integer($int64)|Le numéro unique de l'opération|1119920371||
|categorie_personne|string|Indique la catégorie de personne impliquée dans le bilan humain|Pêcheur français||
|resultat_humain|string|Description du bilan humain|Personne secourue||
|nombre|number($int32)|Nombre de personnes impliquées dans ce bilan|3|minimum: 0|
|dont_nombre_blesse|number($int32)|Indique le nombre de personnes blessées dans le bilan|1|minimum: 0|

## Installation
```
pip install open_api_schemas_to_markdown
```

## Usage
The package provides a command line tool.
```
$ oa-to-md -h
usage: oa-to-md [-h] input_filepath output_filepath

positional arguments:
  input_filepath   The OpenAPI 3 YAML filepath
  output_filepath  The desired output filepath of the Markdown file

optional arguments:
  -h, --help       show this help message and exit
```

Example:
```
oa-to-md open_api.yml documentation.md
```

## Notice
This software is available under the MIT license and was developed as part of the [Entrepreneur d'Intérêt Général program](https://entrepreneur-interet-general.etalab.gouv.fr) by the French government.

Projet développé dans le cadre du programme « [Entrepreneur d’intérêt général](https://entrepreneur-interet-general.etalab.gouv.fr) ».
