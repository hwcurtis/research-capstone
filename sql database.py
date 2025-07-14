CREATE TABLE cleaned_covid_data(
    positive_cases INT NOT NULL,
    negative_cases INT NOT NULL,
    currently_hospitalized INT,
    last_checked_date DATE NOT NULL,
    last_update_et VARCHAR(20),
    total_test_results INT NOT NULL,
    state CHAR(2) NOT NULL,
    recovered_cases INT,
    currently_in_icu INT,
    new_test_results INT NOT NULL
)
