def pad_string(string, beg=True):
    if beg:
        return string + " "
    else:
        return " " + string + " "

def original_phys_perturbation(situation, commonsense_fact, comparison_phrase):
    
    original = situation + " and " + commonsense_fact + ", so A " + comparison_phrase + " B"
   
    return {"original" : original}

def generate_easy_physical_example(initial_comparison,
                                   commonsense_fact,
                                   original_comparison):
    
    output = {}

    output["original"] = original_phys_perturbation(initial_comparison, commonsense_fact, original_comparison)
    
    return output


def original_material_perturbation(material_1, material_2, comparison_phrase):    

    original_premise =  "A is made out of " + material_1 + \
                        ", B is made out of " + material_2 + \
                        " and " + material_1 + pad_string(comparison_phrase, False) + material_2

    original_conclusion = ", so A " + comparison_phrase + " B"

    original = original_premise + original_conclusion


    # asymmetric_p_premise = "B is made out of " + material_1 + \
    #                        ", A is made out of " + material_2 + \
    #                        " and " + material_1 + pad_string(comparison_phrase, False) + material_2

    # asymmetric_p_conclusion = ", so A " + negation_comparison_phrase + " B"

    # asymmetric_premise = asymmetric_p_premise + asymmetric_p_conclusion
    

    # asymmetric_c_premise = "A is made out of " + material_1 + \
    #                        ", B is made out of " + material_2 + \
    #                        " and " + material_1 + pad_string(comparison_phrase, False) + material_2

    # asymmetric_c_conclusion = ", so B " + negation_comparison_phrase + " A"


    # asymmetric_conclusion = asymmetric_c_premise + asymmetric_c_conclusion

    # return {"original" : original,
    #         "asymmetric_premise" : asymmetric_premise,
    #         "asymmetric_conclusion" : asymmetric_conclusion}

    return {"original" : original}


def generate_easy_material_example(material_1,
                                   material_2,
                                   original_comparison):

    output = {}

    output["original"] = original_material_perturbation(material_1, material_2, original_comparison)

    return output

def original_social_perturbation(situation, commonsense_fact, comparison_phrase):
    
    original = situation + " and " + commonsense_fact + ", so A " + comparison_phrase + " B"

    return {"original" : original}

def generate_easy_social_example(initial_comparison,
                                 commonsense_fact,
                                 original_comparison):

    output = {}

    output["original"] = original_social_perturbation(initial_comparison, commonsense_fact, original_comparison)
   

    return output