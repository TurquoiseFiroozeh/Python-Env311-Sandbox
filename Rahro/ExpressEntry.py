"This code is all about express entry program"


def IsEligible():
    "This function is for asking some questions to assess the candidates eligibility for express entry"

    global NATIONALITY
    global AGE
    global LANGUAGE_ABILITY
    global LANGUAGE_TEST_DATE
    global LANGUAGE_SPEAKING_SCORE
    global LANGUAGE_LISTENING_SCORE
    global LANGUAGE_READING_SCORE
    global LANGUAGE_WRITING_SCORE
    global FAMILY_MEMBERS
    global EDUCATION
    global WORK_EXPERIENCE
    global AVAILABLE_FUNDS
    global DETAILS_ON_ANY_JOB_OFFER
    global INTERESTED_PROVINCE
    global OTHER_LANGUAGE

    INTERESTED_PROVINCE = input(
        "Choose the province or territory you are the most interested in?")
    LANGUAGE_ABILITY = input(
        "Which language test did you take for your first official language?")
    LANGUAGE_TEST_DATE = input(
        "What date did you take language test?(YYYY-MM-DD)")
    LANGUAGE_SPEAKING_SCORE = input("Enter the test score for speaking?")
    LANGUAGE_LISTENING_SCORE = input("Enter the test score for listening?")
    LANGUAGE_READING_SCORE = input("Enter the test score for reading?")
    LANGUAGE_WRITING_SCORE = input("Enter the test score for writing?")
    OTHER_LANGUAGE = input("Other Language?")
    return False


print(IsEligible())
