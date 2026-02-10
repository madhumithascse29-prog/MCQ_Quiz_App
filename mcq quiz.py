def run_quiz():
    score = 0

    print("----- Welcome to the Science Quiz -----")

    for i in range(1, 21):

        if i == 1:
            question = "What is the chemical symbol for water?"
            print("A. H2O  B. O2  C. CO2  D. NaCl")
            correct = "A"

        elif i == 2:
            question = "Which planet is known as the Red Planet?"
            print("A. Venus  B. Mars  C. Jupiter  D. Saturn")
            correct = "B"

        elif i == 3:
            question = "What gas do plants absorb from the atmosphere?"
            print("A. Oxygen  B. Nitrogen  C. Carbon Dioxide  D. Hydrogen")
            correct = "C"

        elif i == 4:
            question = "What is the boiling point of water at sea level?"
            print("A. 50°C  B. 75°C  C. 100°C  D. 120°C")
            correct = "C"

        elif i == 5:
            question = "Which organ in the human body pumps blood?"
            print("A. Brain  B. Lungs  C. Heart  D. Liver")
            correct = "C"

        elif i == 6:
            question = "Which gas is most abundant in the Earth's atmosphere?"
            print("A. Oxygen  B. Nitrogen  C. Carbon Dioxide  D. Hydrogen")
            correct = "B"

        elif i == 7:
            question = "What is the center of an atom called?"
            print("A. Electron  B. Proton  C. Nucleus  D. Neutron")
            correct = "C"

        elif i == 8:
            question = "Which vitamin is produced when sunlight hits the skin?"
            print("A. Vitamin A  B. Vitamin B  C. Vitamin C  D. Vitamin D")
            correct = "D"

        elif i == 9:
            question = "What is the chemical formula of table salt?"
            print("A. NaCl  B. KCl  C. CaCl2  D. HCl")
            correct = "A"

        elif i == 10:
            question = "Which planet has the largest size in our solar system?"
            print("A. Earth  B. Jupiter  C. Saturn  D. Mars")
            correct = "B"

        elif i == 11:
            question = "Which part of the plant conducts photosynthesis?"
            print("A. Root  B. Stem  C. Leaf  D. Flower")
            correct = "C"

        elif i == 12:
            question = "Which is the hardest natural substance?"
            print("A. Gold  B. Iron  C. Diamond  D. Silver")
            correct = "C"

        elif i == 13:
            question = "Which organ helps in digestion of food?"
            print("A. Brain  B. Stomach  C. Lungs  D. Heart")
            correct = "B"

        elif i == 14:
            question = "What is the speed of light?"
            print("A. 3×10^8 m/s  B. 3×10^6 m/s  C. 3×10^5 m/s  D. 3×10^7 m/s")
            correct = "A"

        elif i == 15:
            question = "Which blood cells help in fighting infections?"
            print("A. Red blood cells  B. White blood cells  C. Platelets  D. Plasma")
            correct = "B"

        elif i == 16:
            question = "Which gas is used in balloons to make them float?"
            print("A. Oxygen  B. Helium  C. Carbon Dioxide  D. Nitrogen")
            correct = "B"

        elif i == 17:
            question = "Which is the smallest unit of life?"
            print("A. Atom  B. Cell  C. Molecule  D. Organ")
            correct = "B"

        elif i == 18:
            question = "Which part of the eye controls the amount of light entering?"
            print("A. Retina  B. Cornea  C. Pupil  D. Lens")
            correct = "C"

        elif i == 19:
            question = "What force keeps us on the ground?"
            print("A. Magnetism  B. Gravity  C. Friction  D. Inertia")
            correct = "B"

        elif i == 20:
            question = "Which organ removes waste from the blood?"
            print("A. Heart  B. Liver  C. Kidney  D. Lungs")
            correct = "C"

        print("\nQuestion", i, ":", question)
        ans = input("Enter your answer (A/B/C/D): ").upper()

        if ans == correct:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! Correct answer is", correct, "\n")

    print("----- Quiz Finished -----")
    print("Your Score:", score, "/ 20")

    if score == 20:
        print("Excellent!")
    elif score >= 15:
        print("Great job!")
    elif score >= 10:
        print("Good effort!")
    else:
        print("Keep practicing!")

run_quiz()
