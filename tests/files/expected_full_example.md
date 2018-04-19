## Operation Model
|Field|Type|Description|Example|Properties|
|---|---|---|---|---|
|operation_id|integer($int64)|Le numéro unique de l'opération|1119920371||
|pourquoi_alerte|string|La catégorie du type d'intervention.|SAR|enum: SAR, MAS, DIV, SUR|
|moyen_alerte|string|Comment l'alerte a-t-elle été donnée|Téléphone mobile à terre||
|qui_alerte|string|Qui a donné l'alerte|Loueur de bateaux||
|categorie_qui_alerte|string|Catégorie du lanceur d'alerte|Autorité maritime française à terre||
|cross|string|CROSS en charge de la coordination de l'opération|Gris-Nez||
|departement|string|Département où se déroule l'opération|Seine-Maritime|nullable: True|
|est_metropolitain|boolean|Indique si l'opération se déroule en France métropolitaine|True||
|evenement|string|Évenement qui a donné lieu à l'opération|Rupture de mouillage||
|categorie_evenement|string|Catégorie de l'événement ayant donné lieu à l'opération|Accidents individuels à personnes embarquées||
|autorite|string|Autorité en charge de la coordination de l'opération|Préfet maritime||
|sous_autorite|string|Sous-autorité en charge de la coordination de l'opération|SG-Mer||
|zone_responsabilite|string|Où se situe l'intervention|Port et accès||
|latitude|number($float)|Latitude de l'opération au format EPSG:4326 WGS84|48.3977||
|longitude|number($float)|Longitude de l'opération au format EPSG:4326 WGS84|-4.955||
|vent_direction|number($int32)|Direction du vent, en degrès|42|nullable: True<br>minimum: 0<br>maximum: 360|
|vent_force|number($int32)|Force du vent selon l'échelle de Beaufort|3|nullable: True<br>minimum: 0<br>maximum: 12|
|mer_force|number($int32)|État de la mer selon l'échelle de Douglas|3|nullable: True<br>minimum: 0<br>maximum: 9|
|date_heure_reception_alerte|string($date-time)|Date et heure de réception de l'alerte en UTC au format ISO8601|1992-12-06T15:07:00Z||
|date_heure_fin_operation|string($date-time)|Date et heure de fin de l'opération en UTC au format ISO8601|1992-12-06T15:07:00Z||
|numero_sitrep|integer($int32)|Numéro de situation report. Les numéros de SITREP sont remis à 0 tous les ans au 1er janvier 0h heure UTC et est incrémentale par la suite. La numérotation des SITREP est idépendante par les CROSS.||minimum: 1|
|cross_sitrep|string|Numéro unique identifiant l'opération utilisant le CROSS coordinateur de l'opération et le numéro de SITREP|Corsen 2017/42||
|fuseau_horaire|string|Fuseau horaire du CROSS coordonnant l'opération. Le fuseau horaire correspond à la timezone database de l'IANA|Europe/Paris||
## ResultatHumain Model
|Field|Type|Description|Example|Properties|
|---|---|---|---|---|
|operation_id|integer($int64)|Le numéro unique de l'opération|1119920371||
|categorie_personne|string|Indique la catégorie de personne impliquée dans le bilan humain|Pêcheur français||
|resultat_humain|string|Description du bilan humain|Personne secourue||
|nombre|number($int32)|Nombre de personnes impliquées dans ce bilan|3|minimum: 0|
|dont_nombre_blesse|number($int32)|Indique le nombre de personnes blessées dans le bilan|1|minimum: 0|
## Moyen Model
|Field|Type|Description|Example|Properties|
|---|---|---|---|---|
|operation_id|integer($int64)|Le numéro unique de l'opération|1119920371||
|numero_ordre|integer($int32)|Indique l'ordre de déploiement des moyens. Le premier moyen mis en oeuvre est numéroté 1, le suivant 2 etc.|1||
|moyen|string|Une description du moyen mis en oeuvre|Hélicoptère léger||
|categorie_moyen|string|Catégorie du moyen mis en oeuvre|Avion-Hélicoptère||
|domaine_action|string|Domaine d'action du moyen mis en oeuvre|Nautique|enum: Nautique, Terrestre, Aérien|
|autorite_moyen|string|Autorité de rattachement du moyen mis en oeuvre|Gendarmerie Nationale||
|date_heure_debut|string($date-time)|Date et heure de mise en oeuvre du moyen en UTC au format ISO8601|1992-12-06T15:07:00Z||
|date_heure_fin|string($date-time)|Date et heure de fin de mise en oeuvre du moyen en UTC au format ISO8601|1992-12-06T15:07:00Z||
## Flotteur Model
|Field|Type|Description|Example|Properties|
|---|---|---|---|---|
|operation_id|integer($int64)|Le numéro unique de l'opération|1119920371||
|numero_ordre|integer($int32)|Indique l'ordre d'implication des flotteurs. Le premier flotteur impliqué est numéroté 1, le suivant 2 etc.|1||
|pavillon|string|Indique si le pavillon du flotteur impliqué est français ou étranger|Français|enum: Étranger, Français|
|resultat_flotteur|string|État du flotteur à la fin de l'intervention|Remorqué||
|type_flotteur|string|Indique le type précis du flotteur|Planche à voile||
|categorie_flotteur|string|Grande catégorie à laquelle appartient le flotteur|Plaisance|enum: Commerce, Pêche, Plaisance, Loisir nautique, Aéronef, Autre|
|numero_immatriculation|string|Numéro d'immatriculation du navire|0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33||
|marque|string|Marque du flotteur|SOPA||
|nom_serie|string|Nom de série|CYRUS||
|assurance|boolean|Indique si le flotteur possède une assurance|True|nullable: True|
|longueur|number($float)|Longueur du flotteur en mètres|4.5|nullable: True|
|largeur|number($float)|Largeur du flotteur en mètres|1.67|nullable: True|
|jauge|number($float)|Jauge du flotteur en tonneaux|5.24|nullable: True|
|nombre_personne_recommande|number($int32)|Nombre de personnes recommandées à bord du flotteur|8|nullable: True|
|puissance_maximum_autorisee|number($float)|Puissance maximum autorisée sur le flotteur en kilowatt|7.36|nullable: True|
|surface_voilure|number($float)|Surface de la voilure en mètres carré|39.3|nullable: True|
|puissance_moteurs|number($float)|Puissance totale des moteurs du flotteur en kilowatt|25.76|nullable: True|
|coque|string|Type de coque du flotteur|MONOCOQUE HABITABLE|nullable: True|
|materiau|string|Matériau de construction du navire|POLYESTER/EPOXY|nullable: True|
|propulsion|string|Mode de propulsion du flotteur|Moteur à essence|nullable: True|
|type_moteur|string|Type de moteur|HORS-BORD|nullable: True|
|type_navire|string|Type du navire|VOILIER|nullable: True|
|utilisation|string|Quel usage est fait du flotteur|USAGE PERSONNEL|nullable: True|
