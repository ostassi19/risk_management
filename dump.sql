INSERT INTO `damage` (`id`, `security_impact`, `consequence_type`, `name`, `damage_type`, `comment`, `selection`) VALUES
(1, 'Disponibilité', 'Indisponibilité', 'Inac', 'Inaccessibilité', 'L\'élément est introuvable : absence d\'adresse, adresse fausse ou service assurant l\'adressage indisponible', NULL),
(2, 'Disponibilité', 'Indisponibilité', 'Disp', 'Disparition', 'L\'élément est absent là où on le cherche (et pour un prestataire, il n\'est plus opérationnel)', NULL),
(3, 'Disponibilité', 'Indisponibilité', 'Endp', 'Endommagement physique', 'Endommagement physique (détecté) rendant l\'élément matériel non fonctionnel', NULL),
(4, 'Disponibilité', 'Indisponibilité', 'Endl', 'Endommagement logique', 'Endommagement logique(détecté) rendant l\'élément non fonctionnel (programmes non fonctionnels, données incohérentes)', NULL),
(5, 'Disponibilité', 'Indisponibilité', 'Inop', 'Inopérabilité', 'L\'élément reste, en lui même, fonctionnel mais ne peut être mis en opération pour des raisons exogènes (absence de personnel, de service indispensable au fonctionnement, etc.)', NULL),
(6, 'Disponibilité', 'Indisponibilité', 'Inex', 'Inexploitabilité', 'L\'élément est sans dommage apparent mais non fonctionnel (panne, saturation, perte de performances rédhibitoire, etc.) ou inexploitable soit totalement (élément nécessaire absent : clé de chiffrement, licence, jeton d\'accès, etc. ou ) soit partiellement (dégâts dus à la pollution, au vieillissement) soit à cause d\'un défaut d\'intégrité détecté (dont un défaut de cohérence)', NULL),
(7, 'Intégrité', 'Défaut d\'intégrité', 'Altd', 'Altération (non détectée) de donnée', 'Tout ou partie des données ont été corrompues de manière accidentelle ou malveillante (que ce soit pour un ensemble structuré de données ou pour des données isolées ou messages)', NULL),
(8, '', 'Défaut d\'intégrité', 'Altf', 'Altération (non détectée) de fonction', 'Tout ou partie des fonctionnalités ont été corrompues de manière accidentelle ou malveillante (fonctions logicielles, matérielles ou paramètres de fonctionnement)', NULL),
(9, 'Intégrité', 'Défaut d\'intégrité', 'Inco', 'Incohérence (non détectée) de données', 'L\'ensemble de données comporte des incohérences', NULL),
(10, 'Intégrité', 'Défaut d\'intégrité', 'Crfx', 'Création de faux', 'Un élément nouveau et illégitime a été émis', NULL),
(11, 'Confidentialité', 'Divulgation', 'Dive', 'Divulgation de données', 'Tout ou partie de l\'ensemble de données a été dupliqué, téléchargé, diffusé ou volé', NULL),
(12, 'Efficience des processus', 'Inapplication de procédures adaptées', 'Napp', 'Non application de la procédure adaptée', 'Les procédures adéquates n\'ont pas été suivies par le personnel (par ignorance ou volontairement)', NULL);

INSERT INTO `decision` (`id`, `decision_result`) VALUES
(1, 'Accepter le risque'),
(2, 'Réduire le risque par des mesures de sécurité'),
(3, 'Eviter le risque par des mesures métiers ou organisationnelles'),
(4, 'Transférer le risque'),
(5, 'Déclarer le sénario impossible ou hors domaine'),
(6, 'Absence de décision');

-- --------------------------------------------------------


INSERT INTO `mesure_level` (`id`, `level`, `description`, `definition`) VALUES
(1, 'Niveau 0', 'Il n\'y a pas de mesure dissuasive pour ce scénario', ''),
(2, 'Niveau 1', 'L’effet dissuasif est très faible. ', 'L\'auteur peut logiquement penser qu\'il n\'encourrait aucun risque personnel : il peut penser qu\'il ne serait pas identifié ou qu\'il aurait de très sérieux arguments pour réfuter toute imputation de l\'action ou que les sanctions seraient très faibles.'),
(3, 'Niveau 2', 'L’effet dissuasif est moyen.', 'L\'auteur peut logiquement penser qu\'il encourrait un risque faible et qu\'en tout état de cause les préjudices personnels qu\'il aurait à subir resteraient supportables.'),
(4, 'Niveau 3', 'L’effet dissuasif est important.', 'Un auteur rationnel devrait logiquement penser qu\'il encourt un risque important: il devrait savoir qu\'il serait sans doute identifié et que les préjudices qu\'il aurait à subir seraient graves.'),
(5, 'Niveau 4', 'L’effet dissuasif est très important.', 'Un auteur rationnel devrait logiquement abandonner toute idée d\'action. Il devrait savoir qu\'il sera presque certainement démasqué et que les sanctions encourues sont hors de proportion avec le gain espéré.');


INSERT INTO `primary_actif` (`id`, `code`, `description`, `complementary_description`, `actif_type`, `impact_level`) VALUES
(1, 'D01', 'Données applicatives', 'Données contenues dans des fichiers ou bases de données utilisés par les appplications', 'Données et informations ', NULL),
(2, 'D02', 'Données bureautiques', 'Données contenues dans des fichiers personnels ou partagés, incluant les fichiers d\'agenda ou de contacts', 'Données et informations ', NULL),
(3, 'D03', 'Informations écrites ou imprimées', 'détenues par les utilisateurs, archives personnelles, listings et états imprimés issus des applications informatiques, et la documentation des processus et autres actifs pouvant être nécessaire à l\'activité.', 'Données et informations ', NULL),
(4, 'D04', 'Courrier électronique ou postal', ' Courrier électronique, postal ou télécopies', 'Données et informations ', NULL),
(5, 'D05', 'Archives ', 'patrimoniales, documentaires ou informatiques', 'Données et informations ', NULL),
(6, 'D06', 'Données et informations publiées ', 'sur des sites publics ou internes', 'Données et informations ', NULL),
(7, 'D07', 'Données externalisées', 'sur le cloud', 'Données et informations ', NULL),
(8, 'S01', 'Services applicatifs', 'applications métiers, services bureautiques ou systèmes communs', ' Services informatiques', NULL),
(9, 'S02', 'Services externalisés', 'ou hébergés sur le cloud', ' Services informatiques', NULL),
(10, 'S03', 'Services de publication d\'informations ', 'sur un site web interne ou public', ' Services informatiques', NULL),
(11, 'P01', 'Processus de gestion de la conformité ', 'aux exigences légales ou contractuelles ou de l\'entité', 'Processus de management et de gestion', NULL),
(12, 'P02', 'Processus de gouvernance et de prise de décision ', 'dans la gouvernance de l’entité (pouvant conduire à un dysfonctionnement redouté) y compris la gouvernance de la sécurité', 'Processus de management et de gestion', NULL);


INSERT INTO `support_actif` (`id`, `name`, `type`, `element`, `selection`) VALUES
(1, 'Fic', 'Fichier ou base de données ', '\"Eléménts immatériels de type \"\"données\"\"\"', NULL),
(2, 'Det', 'Données en transit', '\"Eléménts immatériels de type \"\"données\"\"\"', NULL),
(3, 'Coe', 'Courriel en transit', '\"Eléménts immatériels de type \"\"données\"\"\"', NULL),
(4, 'Med', 'Media support de données', 'Eléments matériels supports de données (ou d\'information)', NULL),
(5, 'Doc', 'Document', 'Eléments matériels supports de données (ou d\'information)', NULL),
(6, 'Cop', 'Courrier en transit', 'Eléments matériels supports de données (ou d\'information)', NULL),
(7, 'Msa', 'Média support d\'archive', 'Eléments matériels supports de données (ou d\'information)', NULL),
(8, 'Cfg', 'Configuration systèmes et applications', '\"Eléments immatériels de type \"\"services\"\"\"', NULL),
(9, 'Equ', 'Equipement de l\'Infrastructure informatique', 'Eléments matériels supports de services ', NULL),
(10, 'Env', 'Environnement de travail et équipement des utilisateurs', 'Eléments matériels supports de services ', NULL),
(11, 'Msl', 'Media support de logiciel', 'Eléments matériels supports de services ', NULL),
(12, 'Iml', 'Infrastructure matérielle et logicielle support de services externalisés', '\"Eléments mixtes de type \"\"services\"\"\"', NULL),
(13, 'Pro', ' Procédure support des processus', '\"Eléments immatériels de type \"\"processus\"\"\"', NULL);

-- --------------------------------------------------------


INSERT INTO `trigger_event` (`id`, `code_type`, `type`, `code`, `event`, `standard_natural_exposure`, `decision_natural_exposure`, `result_natural_exposure`, `comment`, `selection`) VALUES
(1, 'AB.P', 'Absence de personnel', 'AB.P.Per', 'Absence accidentelle de personnel interne ou de partenaire', 3, 0, 3, '', NULL),
(2, 'AB.S', 'Absence ou indisponibilité accidentelle de service', 'AB.S.Gen', 'Absence de services généraux : défaillance ou indisponibilité de services généraux ou de servitudes, énergie, climatisation, etc.', 2, 0, 2, '', NULL),
(3, 'AB.S', 'Absence ou indisponibilité accidentelle de service', 'AB.S.Loc', 'Absence de service : Impossibilité d\'accès aux locaux', 2, 0, 2, '', NULL),
(4, 'AB.S', 'Absence ou indisponibilité accidentelle de service', 'AB.S.Mat', 'Absence de matériel compatible ou incompatibilité de systèmes', 2, 0, 2, '', NULL),
(5, 'AB.S', 'Absence ou indisponibilité accidentelle de service', 'AB.S.Ser', 'Absence de service : défaillance ou indisponibilité des services fournis par un prestataire externe', 3, 0, 3, '', NULL),
(6, 'AC.E', 'Accident grave d\'environnement', 'AC.E.Evt', 'Accident grave d\'environnement : Incendie, Inondation, foudroiement, tremblement de terre… ou dû à du terrorisme', 2, 0, 2, '', NULL),
(7, 'AC.M', 'Accident matériel', 'AC.M.Equ', 'Panne ou dysfonctionnement d\'équipement', 3, 0, 3, '', NULL),
(8, 'AH.L', 'Action humaine (délibérée ou non) menée par voie logique ou fonctionnelle', 'AH.L.Blo', 'Attaque en blocage de comptes', 2, 0, 2, '', NULL),
(9, 'AH.L', 'Action humaine (délibérée ou non) menée par voie logique ou fonctionnelle', 'AH.L.Cap', 'Captation de données ou messages en transit', 2, 0, 2, '', NULL),
(10, 'AH.L', 'Action humaine (délibérée ou non) menée par voie logique ou fonctionnelle', 'AH.L.Cav', 'Captation visuelle de données ', 3, 0, 3, '', NULL),
(11, 'AH.L', 'Action humaine (délibérée ou non) menée par voie logique ou fonctionnelle', 'AH.L.Cfg', 'Effacement volontaire ou pollution massive de configurations systèmes', 2, 0, 2, '', NULL),
(12, 'AH.L', 'Action humaine (délibérée ou non) menée par voie logique ou fonctionnelle', 'AH.L.Del', 'Effacement délibéré de supports logiques ou physiques', 3, 0, 3, '', NULL),
(13, 'AH.L', 'Action humaine (délibérée ou non) menée par voie logique ou fonctionnelle', 'AH.L.Fal', 'Falsification logique (données ou fonctions)', 3, 0, 3, '', NULL),
(14, 'AH.L', 'Action humaine (délibérée ou non) menée par voie logique ou fonctionnelle', 'AH.L.Fau', 'Création de faux (messages ou données)', 3, 0, 3, '', NULL),
(15, 'AH.L', 'Action humaine (délibérée ou non) menée par voie logique ou fonctionnelle', 'AH.L.Kyl', 'Captation de données par Keylogger logiciel', 3, 0, 3, '', NULL),
(16, 'AH.L', 'Action humaine (délibérée ou non) menée par voie logique ou fonctionnelle', 'AH.L.Phi', 'Action menée par abus de confiance (Phishing)', 3, 0, 3, '', NULL),
(17, 'AH.L', 'Action humaine (délibérée ou non) menée par voie logique ou fonctionnelle', 'AH.L.Sam', 'Saturation malveillante d\'équipements informatiques ou réseaux', 3, 0, 3, '', NULL),
(18, 'AH.L', 'Action humaine (délibérée ou non) menée par voie logique ou fonctionnelle', 'AH.L.Tot', 'Destruction logique totale (fichiers et leurs sauvegardes)', 2, 0, 2, '', NULL),
(19, 'AH.L', 'Action humaine (délibérée ou non) menée par voie logique ou fonctionnelle', 'AH.L.Vol', 'Détournement logique de fichiers ou données (téléchargement ou copie)', 3, 0, 3, '', NULL),
(20, 'AH.P', 'Action humaine menée par voie physique', 'AH.P.Fal', 'Manipulation ou falsification matérielle d\'équipement ou de media', 2, 0, 2, '', NULL),
(21, 'AH.P', 'Action humaine menée par voie physique', 'AH.P.Kyp', 'Captation de données par Keylogger physique', 3, 0, 3, '', NULL),
(22, 'AH.P', 'Action humaine menée par voie physique', 'AH.P.Phc', 'Duplication, photocopie ou consultation de media physique ', 3, 0, 3, '', NULL),
(23, 'AH.P', 'Action humaine menée par voie physique', 'AH.P.Vol', 'Vol ou substitution physique ', 3, 0, 3, '', NULL),
(24, 'ER.P', 'Erreur matérielle ou de comportement du personnel', 'ER.P.Peo', 'Perte ou oubli de document ou de media', 3, 0, 3, '', NULL),
(25, 'ER.P', 'Erreur matérielle ou de comportement du personnel', 'ER.P.Pro', 'Erreur de manipulation ou dans le suivi d\'une procédure', 3, 0, 3, '', NULL),
(26, 'ER.P', 'Erreur matérielle ou de comportement du personnel', 'ER.P.Prs', 'Erreur de saisie ou de frappe', 3, 0, 3, '', NULL),
(27, 'IC.E', 'Incident dû à l\'environnement', 'IC.E.Div', 'Dégâts divers dus à l\'environnement (vieillissement, pollution, dégâts des eaux, surcharge électrique, etc.) ou à du vandalisme', 2, 0, 2, '', NULL),
(28, 'IF.L', 'Incident logique ou fonctionnel', 'IF.L.Lsp', 'Bug bloquant dans un logiciel système, middleware, applicatif ou un progiciel', 2, 0, 2, '', NULL),
(29, 'IF.L', 'Incident logique ou fonctionnel', 'IF.L.Vir', 'Logiciel malveillant ou virus', 4, 0, 4, '', NULL),
(30, 'PR.N', 'Procédures adéquates non appliquées', 'PR.N.Nai', 'Procédures adéquates absentes ou méconnues', 2, 0, 2, '', NULL),
(31, 'PR.N', 'Procédures adéquates non appliquées', 'PR.N.Nar', 'Conflit non ou mal résolu entre procédures', 2, 0, 2, '', NULL),
(32, 'PR.N', 'Procédures adéquates non appliquées', 'PR.N.Nav', 'Procédures inappliquées volontairement', 2, 0, 2, '', NULL);

