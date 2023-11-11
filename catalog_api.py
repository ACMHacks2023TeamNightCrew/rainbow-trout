import requests
from bs4 import BeautifulSoup

DEPARTMENTS = {'acen': 'acen-academic-english', 'am': 'am-applied-mathematics', 'anth': 'anth-anthropology',
               'aplx': 'aplx-applied-linguistics', 'arbc': 'arbc-arabic', 'art': 'art-art',
               'artg': 'artg-art-and-design-games-and-playable-media', 'astr': 'astr-astronomy-and-astrophysics',
               'bioc': 'bioc-biochemistry-and-molecular-biology', 'bioe': 'bioe-biology-ecology-and-evolutionary',
               'biol': 'biol-biology-molecular-cell-and-developmental', 'bme': 'bme-biomolecular-engineering',
               'chem': 'chem-chemistry-and-biochemistry', 'chin': 'chin-chinese', 'clni': 'clni-college-nine',
               'clst': 'clst-classical-studies', 'cmmu': 'cmmu-community-studies', 'cmpm': 'cmpm-computational-media',
               'cowl': 'cowl-cowell-college', 'cres': 'cres-critical-race-and-ethnic-studies',
               'crsn': 'crsn-carson-college', 'crwn': 'crwn-crown-college',
               'cse': 'cse-computer-science-and-engineering', 'csp': 'csp-coastal-science-and-policy',
               'danm': 'danm-digital-arts-and-new-media', 'eart': 'eart-earth-sciences',
               'ece': 'ece-electrical-and-computer-engineering', 'econ': 'econ-economics', 'educ': 'educ-education',
               'envs': 'envs-environmental-studies', 'esci': 'esci-environmental-sciences',
               'film': 'film-film-and-digital-media', 'fmst': 'fmst-feminist-studies', 'fren': 'fren-french',
               'game': 'game-games-and-playable-media', 'gch': 'gch-global-community-health', 'germ': 'germ-german',
               'grad': 'grad-graduate', 'gree': 'gree-greek', 'havc': 'havc-history-of-art-and-visual-culture',
               'hebr': 'hebr-hebrew', 'hisc': 'hisc-history-of-consciousness', 'his': 'his-history',
               'hci': 'hci-human-computer-interaction', 'ital': 'ital-italian', 'japn': 'japn-japanese',
               'jrlc': 'jrlc-john-r-lewis-college', 'jwst': 'jwst-jewish-studies', 'krsg': 'krsg-kresge-college',
               'laad': 'laad-languages', 'lals': 'lals-latin-american-and-latino-studies', 'latn': 'latn-latin',
               'lgst': 'lgst-legal-studies', 'ling': 'ling-linguistics', 'lit': 'lit-literature',
               'math': 'math-mathematics', 'merr': 'merr-merrill-college',
               'metx': 'metx-microbiology-and-environmental-toxicology', 'musc': 'musc-music',
               'nlp': 'nlp-natural-language-processing', 'oaks': 'oaks-oakes-college', 'ocea': 'ocea-ocean-sciences',
               'pbs': 'pbs-physical-biological-sciences', 'pers': 'pers-persian', 'phil': 'phil-philosophy',
               'phye': 'phye-physical-education', 'phys': 'phys-physics', 'poli': 'poli-politics',
               'port': 'port-portuguese', 'prtr': 'prtr-porter-college', 'psyc': 'psyc-psychology',
               'punj': 'punj-punjabi', 'russ': 'russ-russian', 'scic': 'scic-science-communication',
               'socd': 'socd-social-documentation', 'socy': 'socy-sociology', 'span': 'span-spanish',
               'sphs': 'sphs-spanish-for-heritage-speakers', 'stat': 'stat-statistics',
               'stev': 'stev-stevenson-college', 'thea': 'thea-theater-arts',
               'tim': 'tim-technology-information-management', 'ucdc': 'ucdc-ucdc', 'writ': 'writ-writing',
               'yidd': 'yidd-yiddish'}

MAJORS = {
    'Agroecology B.A.': '/en/current/general-catalog/academic-units/social-sciences-division/environmental-studies/agroecology-ba',
    'Anthropology B.A.': '/en/current/general-catalog/academic-units/social-sciences-division/anthropology/anthropology-ba',
    'Applied Linguistics and Multilingualism B.A.': '/en/current/general-catalog/academic-units/humanities-division/languages-and-applied-linguistics/applied-linguistics-and-multilingualism-ba',
    'Applied Mathematics B.S.': '/en/current/general-catalog/academic-units/baskin-engineering/applied-mathematics/applied-mathematics-bs',
    'Applied Physics B.S.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/physics/applied-physics-bs',
    'Art & Design: Games + Playable Media B.A.': '/en/current/general-catalog/academic-units/arts-division/performance-play-and-design/art-design-games-playable-media-ba',
    'Art B.A.': '/en/current/general-catalog/academic-units/arts-division/art/art-ba',
    'Biochemistry and Molecular Biology B.S.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/chemistry-and-biochemistry/biochemistry-and-molecular-biology-bs',
    'Biology B.A.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/ecology-and-evolutionary-biology/biology-ba',
    'Biology B.S.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/molecular-cell-and-developmental-biology/biology-bs',
    'Biomolecular Engineering and Bioinformatics B.S.': '/en/current/general-catalog/academic-units/baskin-engineering/biomolecular-engineering/biomolecular-engineering-and-bioinformatics-bs',
    'Biotechnology B.A.': '/en/current/general-catalog/academic-units/baskin-engineering/biomolecular-engineering/biotechnology-ba',
    'Business Management Economics B.A.': '/en/current/general-catalog/academic-units/social-sciences-division/economics/business-management-economics-ba',
    'Chemistry B.A.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/chemistry-and-biochemistry/chemistry-ba',
    'Chemistry B.S.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/chemistry-and-biochemistry/chemistry-bs',
    'Classical Studies B.A.': '/en/current/general-catalog/academic-units/humanities-division/history/classical-studies-ba',
    'Cognitive Science B.S.': '/en/current/general-catalog/academic-units/social-sciences-division/psychology/cognitive-science-bs',
    'Community Studies B.A.': '/en/current/general-catalog/academic-units/social-sciences-division/community-studies/community-studies-ba',
    'Computer Engineering B.S.': '/en/current/general-catalog/academic-units/baskin-engineering/computer-science-and-engineering/computer-engineering-bs',
    'Computer Science B.A.': '/en/current/general-catalog/academic-units/baskin-engineering/computer-science-and-engineering/computer-science-ba',
    'Computer Science B.S.': '/en/current/general-catalog/academic-units/baskin-engineering/computer-science-and-engineering/computer-science-bs',
    'Computer Science: Computer Game Design B.S.': '/en/current/general-catalog/academic-units/baskin-engineering/computational-media/computer-science-computer-game-design-bs',
    'Critical Race and Ethnic Studies B.A.': '/en/current/general-catalog/academic-units/humanities-division/critical-race-and-ethnic-studies/critical-race-and-ethnic-studies-ba',
    'Earth Sciences B.S.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/earth-and-planetary-sciences/earth-sciences-bs',
    'Earth Sciences/Anthropology Combined Major B.A.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/earth-and-planetary-sciences/earth-sciencesanthropology-combined-major-ba',
    'Ecology and Evolution B.S.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/ecology-and-evolutionary-biology/ecology-and-evolution-bs',
    'Economics B.A.': '/en/current/general-catalog/academic-units/social-sciences-division/economics/economics-ba',
    'Economics/Mathematics Combined B.A.': '/en/current/general-catalog/academic-units/social-sciences-division/economics/economicsmathematics-combined-ba',
    'Education, Democracy, and Justice B.A.': '/en/current/general-catalog/academic-units/social-sciences-division/education/education-democracy-and-justice-ba',
    'Electrical Engineering B.S.': '/en/current/general-catalog/academic-units/baskin-engineering/electrical-and-computer-engineering/electrical-engineering-bs',
    'Environmental Sciences B.S.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/earth-and-planetary-sciences/environmental-sciences-bs',
    'Environmental Studies B.A.': '/en/current/general-catalog/academic-units/social-sciences-division/environmental-studies/environmental-studies-ba',
    'Environmental Studies/Biology Combined Major B.A.': '/en/current/general-catalog/academic-units/social-sciences-division/environmental-studies/environmental-studiesbiology-combined-major-ba',
    'Environmental Studies/Earth Sciences Combined Major B.A.': '/en/current/general-catalog/academic-units/social-sciences-division/environmental-studies/environmental-studiesearth-sciences-combined-major-ba',
    'Environmental Studies/Economics Combined Major B.A.': '/en/current/general-catalog/academic-units/social-sciences-division/environmental-studies/environmental-studieseconomics-combined-major-ba',
    'Feminist Studies B.A.': '/en/current/general-catalog/academic-units/humanities-division/feminist-studies/feminist-studies-ba',
    'Film and Digital Media B.A.': '/en/current/general-catalog/academic-units/arts-division/film-and-digital-media/film-and-digital-media-ba',
    'Global and Community Health B.A.': '/en/current/general-catalog/academic-units/social-sciences-division/global-and-community-health-ba/global-and-community-health-ba',
    'Global and Community Health B.S.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/molecular-cell-and-developmental-biology/global-and-community-health-bs',
    'Global Economics B.A.': '/en/current/general-catalog/academic-units/social-sciences-division/economics/global-economics-ba',
    'History B.A.': '/en/current/general-catalog/academic-units/humanities-division/history/history-ba',
    'History of Art and Visual Culture B.A.': '/en/current/general-catalog/academic-units/arts-division/history-of-art-and-visual-culture/history-of-art-and-visual-culture-ba',
    'Human Biology B.S. (Discontinued)': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/molecular-cell-and-developmental-biology/human-biology-bs-discontinued',
    'Jewish Studies B.A.': '/en/current/general-catalog/academic-units/humanities-division/history/jewish-studies-ba',
    'Language Studies B.A.': '/en/current/general-catalog/academic-units/humanities-division/linguistics/language-studies-ba',
    'Latin American and Latino Studies B.A.': '/en/current/general-catalog/academic-units/social-sciences-division/latin-american-and-latino-studies/latin-american-and-latino-studies-ba',
    'Latin American and Latino Studies/Politics Combined B.A.': '/en/current/general-catalog/academic-units/social-sciences-division/latin-american-and-latino-studies/latin-american-and-latino-studiespolitics-combined-ba',
    'Latin American and Latino Studies/Sociology Combined B.A.': '/en/current/general-catalog/academic-units/social-sciences-division/latin-american-and-latino-studies/latin-american-and-latino-studiessociology-combined-ba',
    'Legal Studies B.A.': '/en/current/general-catalog/academic-units/social-sciences-division/politics/legal-studies-ba',
    'Linguistics B.A.': '/en/current/general-catalog/academic-units/humanities-division/linguistics/linguistics-ba',
    'Literature B.A.': '/en/current/general-catalog/academic-units/humanities-division/literature/literature-ba',
    'Marine Biology B.S.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/ecology-and-evolutionary-biology/marine-biology-bs',
    'Mathematics B.A.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/mathematics/mathematics-ba',
    'Mathematics B.S.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/mathematics/mathematics-bs',
    'Mathematics Education B.A.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/mathematics/mathematics-education-ba',
    'Mathematics Theory and Computation B.S.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/mathematics/mathematics-theory-and-computation-bs',
    'Microbiology B.S.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/microbiology-and-environmental-toxicology/microbiology-bs',
    'Molecular, Cell, and Developmental Biology B.S.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/molecular-cell-and-developmental-biology/molecular-cell-and-developmental-biology-bs',
    'Music B.A.': '/en/current/general-catalog/academic-units/arts-division/music/music-ba',
    'Music B.M.': '/en/current/general-catalog/academic-units/arts-division/music/music-bm',
    'Network and Digital Technology B.A.': '/en/current/general-catalog/academic-units/baskin-engineering/computer-science-and-engineering/network-and-digital-technology-ba',
    'Neuroscience B.S.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/molecular-cell-and-developmental-biology/neuroscience-bs',
    'Philosophy B.A.': '/en/current/general-catalog/academic-units/humanities-division/philosophy/philosophy-ba',
    'Physics (Astrophysics) B.S.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/physics/physics-astrophysics-bs',
    'Physics B.S.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/physics/physics-bs',
    'Plant Sciences B.S.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/ecology-and-evolutionary-biology/plant-sciences-bs',
    'Politics B.A.': '/en/current/general-catalog/academic-units/social-sciences-division/politics/politics-ba',
    'Psychology B.A.': '/en/current/general-catalog/academic-units/social-sciences-division/psychology/psychology-ba',
    'Robotics Engineering B.S.': '/en/current/general-catalog/academic-units/baskin-engineering/electrical-and-computer-engineering/robotics-engineering-bs',
    'Science Education B.S.': '/en/current/general-catalog/academic-units/physical-and-biological-sciences-division/physics/science-education-bs',
    'Sociology B.A.': '/en/current/general-catalog/academic-units/social-sciences-division/sociology/sociology-ba',
    'Spanish Studies B.A.': '/en/current/general-catalog/academic-units/humanities-division/languages-and-applied-linguistics/spanish-studies-ba',
    'Technology and Information Management B.S.': '/en/current/general-catalog/academic-units/baskin-engineering/technology-and-information-management/technology-and-information-management-bs',
    'Theater Arts B.A.': '/en/current/general-catalog/academic-units/arts-division/performance-play-and-design/theater-arts-ba'
}


def get_majors():
    descs = dict()
    html = requests.get("https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees/").text
    soup = BeautifulSoup(html, "html.parser")
    ul = soup.find("h1", {"id": "h6779"}).find_next_sibling("ul")
    links = ul.findChildren("a")
    for link in links:
        desc = link.text
        url = link["href"]
        descs[desc] = url
    return descs


def get_department_descriptions():
    descs = dict()
    html = requests.get("https://catalog.ucsc.edu/en/2022-2023/general-catalog/courses/").text
    soup = BeautifulSoup(html, "html.parser")
    ul = soup.find("ul", {"class": "sc-child-item-links"})
    links = ul.findChildren("a")
    for link in links:
        description = link["href"].split("/")[-1].lower()
        dept = description.split("-")[0]
        descs[dept] = description
    return descs


def get_course_level(num):
    n = int(num)
    if n < 100:
        return "lower-division"
    elif n < 200:
        return "upper-division"
    return "graduate"


def get_quarters_offered(course_id):
    dept, num = course_id.split("-")

    url = ("https://catalog.ucsc.edu/en/2022-2023/general-catalog/courses/%s/%s/%s"
           % (DEPARTMENTS[dept], get_course_level(num), course_id))
    html = requests.get(url)

    soup = BeautifulSoup(html.text, "html.parser")
    div = soup.find("div", {"class": "quarter"})
    return div.find("p").text.split(", ")


def get_course_info(course_id):
    dept, num = course_id.split("-")

    url = ("https://catalog.ucsc.edu/en/2022-2023/general-catalog/courses/%s/%s/%s"
           % (DEPARTMENTS[dept], get_course_level(num), course_id))
    html = requests.get(url)

    soup = BeautifulSoup(html.text, "html.parser")
    div = soup.find("div", {"class": "quarter"})
    quarters = div.find("p").text.split(", ")
    description = soup.find("div", {"class": "desc"}).text
    credits_gained = soup.find("div", {"class": "extraFields"}).find("p").text
    instructors = soup.find("div", {"class": "instructor"}).find("p").text

    return {
        "quarters": quarters,
        "description": description,
        "credits": credits_gained,
        "instructors": instructors
    }