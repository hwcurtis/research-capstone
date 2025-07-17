"""
Postural Orthostatic Tachycardia Syndrome (POTS)
POTS is a condition with a wide range of symptoms, which can vary greatly from person to person.
"""

# List of common symptoms associated with POTS
symptoms = [
    "Dizziness or lightheadedness, especially when standing up, during prolonged standing in one position or on long walks.",
    "Fainting or near fainting.",
    "Forgetfulness and trouble focusing (brain fog).",
    "Heart palpitations or racing heart rate.",
    "Exhaustion/fatigue.",
    "Feeling nervous or anxious.",
    "Shakiness and excessive sweating.",
    "Shortness of breath (dyspnea).",
    "Chest pain.",
    "Headaches.",
    "Feeling sick.",
    "Bloating.",
    "A pale face and purple discoloration of your hands and feet if they are lower than the level of your heart.",
    "Disrupted sleep from chest pain, racing heart rate and excessive sweating during sleep."
]

# Situations that can worsen symptoms of POTS
worsening_situations = [
    "Being in warm environments, such as in a hot bath or shower or on a hot day.",
    "Standing frequently, such as when you are waiting in line or shopping.",
    "Participating in strenuous exercise.",
    "When you are sick, such as from a cold or an infection.",
    "Having your period (menstruation)."
]

# Subtypes of POTS and their potential causes
pot_subtypes = {
    "Neuropathic POTS": "Occurs due to peripheral denervation (loss of nerve supply), which leads to poor blood vessel constriction, especially in the legs and abdomen.",
    "Hyperadrenergic POTS": "Occurs when the sympathetic nervous system is overactive, leading to increased levels of norepinephrine.",
    "Hypovolemic POTS": "Results from reduced blood volume, which contributes to symptoms like lightheadedness and fatigue."
}

# Summary statement for ongoing research
research_summary = (
    "Researchers have not identified a single cause of POTS. It is believed to have multiple causes, "
    "and may involve combinations of the above subtypes. There is also growing evidence suggesting POTS can follow viral infections, including COVID-19."
)


# Function to display POTS symptoms
def display_pots_info():
    print("Postural Orthostatic Tachycardia Syndrome (POTS) - Symptoms and Information")
    print("Common Symptoms:")
    for symptom in symptoms:
        print(f" - {symptom}")
    print("\nWorsening Situations:")
    for situation in worsening_situations:
        print(f" - {situation}")
    print("\nPOTS Subtypes:")
    for subtype, description in pot_subtypes.items():
        print(f" - {subtype}: {description}")
    print("\nResearch Summary:")
    print(research_summary)


# Call the function to display the information
display_pots_info()

dysautonomia_symptoms = [
    "Balance problems.",
    "Fainting or passing out (especially when standing up).",
    "Nausea and vomiting.",
    "“Brain fog,” forgetfulness or trouble focusing.",
    "Fast heart rate (tachycardia) or slow heart rate (bradycardia).",
    "Pinpoint eye pupils or unusually wide eye pupils.",
    "Changes in bowel movements (constipation or diarrhea).",
    "Fatigue or ongoing tiredness.",
    "Sexual dysfunction.",
    "Chest pain or discomfort.",
    "Frequent urge to pee (urinate) or urinary incontinence.",
    "Shortness of breath (dyspnea).",
    "Clammy or pale skin.",
    "Heart palpitations.",
    "Sleeping problems.",
    "Trouble swallowing (dysphagia).",
    "Irregular heart rhythm (arrhythmia).",
    "Sound or light sensitivity.",
    "Dizziness or lightheadedness (especially when standing up).",
    "Low blood sugar (hypoglycemia).",
    "Sweating more or less than usual, or sweating more in certain body parts.",
    "Unusually dry or watery eyes.",
    "Migraines or frequent headaches.",
    "Swings in body or skin temperature.",
    "Excessive drooling.",
    "Mood swings or anxiety.",
    "Vision issues (blurred vision or trouble with your eyes adjusting to light changes).",
    "Exercise intolerance (your heart rate doesn’t change with physical activity).",
    "Runny nose.",
    "Vertigo."
]

# Note: The above symptoms are not exclusive to POTS and can be associated with other forms of dysautonomia or autonomic nervous system disorders.

# Function to display dysautonomia symptoms


def display_dysautonomia_info():
    print("Dysautonomia Symptoms:")
    for symptom in dysautonomia_symptoms:
        print(f" - {symptom}")


COVID_symptoms = [
    "Fever",
    "Sore throat",
    "Headache",
    "Tiredness (fatigue)",
    "Body aches",
    "Chills",
    "Stuffy or runny nose",
    "Cough",
    "Shortness of breath",
    "Loss of or altered sense of smell and taste",
    "Difficulty thinking and focusing (brain fog)",
    "Digestive symptoms, like diarrhea, nausea and vomiting"
]


def display_covid_info():
    print("COVID-19 Symptoms:")
    for symptom in COVID_symptoms:
        print(f" - {symptom}")
