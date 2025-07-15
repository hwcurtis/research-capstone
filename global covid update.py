from sqlite3 import sqlite_version

database_path = "global_covid_update.db"


def OpenDatabase(path, persist=True):
    import sqlite3
    conn = sqlite3.connect(path)
    if persist:
        conn.execute("PRAGMA foreign_keys = ON")
    return connn to the global COVID-19 update database.


During the four-week reporting period(11 November to 8 December 2024), weekly SARS-CoV-2 PCR positivity conducted through systematic virological surveillance changed from 9.5 % in the first week of the reporting period to 8.6 % in the last week, with a weekly average of over 56 000 specimens tested across 103 countries with all regions reporting a percent test positivity below elevated level in the last reporting week.
• WHO is monitoring seven SARS-CoV-2 variants, including one variant of interest (VOI) JN.1, and six variants under monitoring (VUMs). JN.1, the VOI, accounted for 16.2 % of sequences in week 49. The VUM, XEC continues to increase in prevalence, accounting for 38.6 % of sequences in week 49, and is currently the most prevalent SARS-CoV-2 variant. All the remaining VUMs are declining in prevalence except JN.1.18, which is presenting a slight increase at a low level (0.7 %).
• Wastewater surveillance, an important component of SARS-CoV-2 surveillance, is also important for early warning and for monitoring SARS-CoV-2 variant circulation. Around 30 countries from five WHO Regions have publicly available wastewater surveillance information and are featured on WHO’s COVID-19 dashboard. According to estimates obtained from wastewater surveillance, circulation of the SARS-CoV-2 virus is approximately 2 to 19 times higher than identified and reported cases * †‡§.
• Globally, during the 28-day period from 11 November to 8 December 2024, 81 countries reported COVID-19 cases, and 31 countries reported COVID-19 deaths. Note that this does not reflect the actual number of countries where cases or deaths occur, as many countries have stopped or changed the frequency of reporting. From the available data, the number of reported cases decreased by 6 % during the 28-day period, with around 200 000 new cases while new deaths decreased by 24 % with over 2600 fatalities, compared to the previous 28 days(14 October to 10 November 2024). Trends in the number of new reported cases and deaths should be interpreted with caution due to decreased testing and sequencing, alongside reporting delays in many countries.
• During the same period, 43 (18 %) countries provided data on COVID-19 hospitalizations and 29 (12%) countries on admissions to an intensive care unit (ICU) at least once, respectively. From available data, about 22 000 new hospitalizations and more than 2000 new ICU admissions were reported during this
* Show us the data: global COVID-19 wastewater monitoring effectors, equity, and gaps
† Capturing the SARS-CoV-2 infection pyramid within the municipality of Rotterdam using longitudinal sewage surveillance
§. The role of wastewater surveillance in understanding the dynamics of SARS-CoV-2 transmission and its variants is crucial for public health responses.


df OpenDatabase(path, persist)
# Open a database connectio


print(sqlite_version)
