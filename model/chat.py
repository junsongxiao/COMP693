

import spacy

# Load spaCy language model

model_path = "D:\\COMP693\\EZT_Booking_System_COMP\\COMP693_NEW\\COMP693\\.venv\\Lib\\site-packages\\en_core_web_sm\\en_core_web_sm-3.7.1"
nlp = spacy.load(model_path)

# Load knowledge base into a dictionary
knowledge_base = {}
tour_name = None  # Initialize tour_name outside the loop

with open('knowledge_base.txt', encoding='UTF-8', mode='r') as f:
    for line in f:
        if line.startswith("#"):
            continue  # Skip comment lines

        tour_info = line.strip().split(":")
        key, value = tour_info[0].strip(), ":".join(tour_info[1:]).strip()

        if key == "Tour Name":
            tour_name = value
            knowledge_base[tour_name] = {
                "location": "",
                "price": 0,
                "features": [],
                "duration": "",
                "reporting_times": [],
                "region": "",
                "additional_info": "",
                "website": "",
                "contact_number": ""
            }
            continue

        if tour_name:  # Ensure tour_name is defined before accessing it
            if key == "Price":
                knowledge_base[tour_name]["price"] = float(value.split()[0][4:])  # Extract just the number
            elif key == "Features":
                knowledge_base[tour_name]["features"] = value.split("\n")  # Split features into a list
            elif key == "Reporting Time":
                knowledge_base[tour_name]["reporting_times"] = value.split(", ")  # Split into list of times
            elif key == "Additional Info":
                knowledge_base[tour_name]["additional_info"] = value
            elif key == "Website":
                knowledge_base[tour_name]["website"] = value
            elif key == "Contact Number":
                knowledge_base[tour_name]["contact_number"] = value
            elif key == "Location":
                knowledge_base[tour_name]["location"] = value

            else:
                # For other keys, assign the value directly if it matches the initialized keys
                if key.replace(" ", "_").lower() in knowledge_base[tour_name]:
                    knowledge_base[tour_name][key.replace(" ", "_").lower()] = value


def process_question(doc, knowledge_base, question_intent):
    """
    Processes a user's question and returns a response based on the knowledge base.

    Args:
        doc (spacy.Doc): The processed user input document.
        knowledge_base (dict): The dictionary containing tour information.

    Returns:
        str: A response to the user's question.
    """

    # Extract keywords and entities from the user input
    keywords = [token.text.lower() for token in doc if token.pos_ in ["NOUN", "PROPN",  "INTJ"]]
    entities = doc.ents  # You can use spaCy's named entity recognition

    # # Identify the user's question intent
    # question_intent = None
    # if "cost" in keywords or "price" in keywords:
    #     question_intent = "price_inquiry"
    # elif "location" in keywords and any(entity.label_ == "GPE" for entity in entities):  # Check for geographical entities
    #     question_intent = "location_inquiry"
    # elif "feature" in keywords or "highlight" in keywords or "activity" in keywords:
    #     question_intent = "features_inquiry"
    # elif "hi" in keywords or "hello" in keywords:
    #     question_intent = "greetings"
    # else:
    #     question_intent = identify_question_intent(doc)

    # # Match keywords and entities to specific information in knowledge base
    # if "hi" in keywords or "hello" in keywords:
    #     question_intent = "greetings"

    matched_tours = []
    

    if question_intent == "greetings":
        response = "Hello! How can I help you today?"

    elif question_intent == "price_inquiry":
        for tour_name, tour_info in knowledge_base.items():
            if any(keyword in tour_name.lower() for keyword in keywords) or any(keyword in feature.lower() for feature in tour_info["features"] for keyword in keywords):
                matched_tours.append(tour_name)
        if matched_tours:
            # Craft a response based on matched tours and their prices:
            response = f"Here are some tours matching your criteria:\n"
            for tour_name in matched_tours:
                tour_info = knowledge_base[tour_name]
                response += f"- {tour_name}: {tour_info['price']}\n"

        else:
            response = "I couldn't find any tours matching your criteria. Please try different keywords or rephrase your question."
    
    elif question_intent == "location_inquiry":
        matched_tours = []

        # Assuming 'location_keywords' are extracted correctly from the user input
        for tour_name, tour_info in knowledge_base.items():
            location_keywords = [kw for kw in keywords if kw in tour_info['location'].lower()]
            # Directly compare the user's location keywords to each tour's location and region
            if any(location_keyword in tour_info['location'].lower() or location_keyword in tour_info['region'].lower() for location_keyword in location_keywords):
                matched_tours.append(tour_name)

        # Add logic for matching named entities (GPEs) against tour locations and regions
        for entity in entities:
            if entity.label_ == "GPE":
                for tour_name, tour_info in knowledge_base.items():
                    if entity.text.lower() in tour_info['location'].lower() or entity.text.lower() in tour_info['region'].lower():
                        matched_tours.append(tour_name)

        if matched_tours:
            response = "Here are some tours in the locations you mentioned:\n"
            for tour_name in matched_tours:
                tour_info = knowledge_base[tour_name]
                response += f"- {tour_name}: {tour_info['location']}\n"
        else:
            response = "I couldn't find any tours in those locations. Please try a different location or specify further."

    elif question_intent == "features_inquiry":
        # Handle feature inquiries:

   
        feature_keywords = [kw for kw in keywords if kw in knowledge_base.values()]
        matched_tours = [tour_name for tour_name, tour_info in knowledge_base.items() if any(feature in tour_info['features'] for feature in feature_keywords)]


        if matched_tours:
            # Craft a response based on matched tours and their features:
            response = f"Here are some tours that match your feature criteria:\n"
            for tour_name in matched_tours:
                tour_info = knowledge_base[tour_name]
                # Highlight matching features for clarity
                relevant_features = [feat for feat in tour_info['features'] if any(kw in feat.lower() for kw in keywords)]
                response += f"- {tour_name}: {', '.join(relevant_features)}\n"
        else:
            response = "I couldn't find any tours with those specific features. Please try different keywords or rephrase your question."
    elif question_intent == "duration_inquiry":
        # Handle duration inquiries:

        duration_keywords = [kw for kw in keywords if kw in knowledge_base.values()]
        matched_tours = [tour_name for tour_name, tour_info in knowledge_base.items() if any(duration in tour_info['duration'] for duration in duration_keywords)]

        if matched_tours:
            # Craft a response based on matched tours and their durations:
            response = f"Here are some tours that match your duration criteria:\n"
            for tour_name in matched_tours:
                tour_info = knowledge_base[tour_name]
                response += f"- {tour_name}: {tour_info['duration']}\n"
        else:
            response = "I couldn't find any tours with those specific durations. Please try different keywords or rephrase your question."
    elif question_intent == "contact_inquiry":
        # Handle contact inquiries:

        contact_keywords = [kw for kw in keywords if kw in knowledge_base.values()]
        matched_tours = [tour_name for tour_name, tour_info in knowledge_base.items() if any(contact in tour_info['contact_number'] for contact in contact_keywords)]

        if matched_tours:
            # Craft a response based on matched tours and their contact numbers:
            response = f"Here are some tours that match your contact criteria:\n"
            for tour_name in matched_tours:
                tour_info = knowledge_base[tour_name]
                response += f"- {tour_name}: {tour_info['contact_number']}\n"
        else:
            response = "I couldn't find any tours with those specific contact numbers. Please try different keywords or rephrase your question."
    elif question_intent == "website_inquiry":
        # Handle website inquiries:

        website_keywords = [kw for kw in keywords if kw in knowledge_base.values()]
        matched_tours = [tour_name for tour_name, tour_info in knowledge_base.items() if any(website in tour_info['website'] for website in website_keywords)]

        if matched_tours:
            # Craft a response based on matched tours and their websites:
            response = f"Here are some tours that match your website criteria:\n"
            for tour_name in matched_tours:
                tour_info = knowledge_base[tour_name]
                response += f"- {tour_name}: {tour_info['website']}\n"
        else:
            response = "I couldn't find any tours with those specific websites. Please try different keywords or rephrase your question."
    elif question_intent == "time_inquiry":
        # Handle time inquiries:

        time_keywords = [kw for kw in keywords if kw in knowledge_base.values()]
        matched_tours = [tour_name for tour_name, tour_info in knowledge_base.items() if any(time in tour_info['reporting_times'] for time in time_keywords)]

        if matched_tours:
            # Craft a response based on matched tours and their reporting times:
            response = f"Here are some tours that match your reporting time criteria:\n"
            for tour_name in matched_tours:
                tour_info = knowledge_base[tour_name]
                response += f"- {tour_name}: {tour_info['reporting_times']}\n"
        else:
            response = "I couldn't find any tours with those specific reporting times. Please try different keywords or rephrase your question."
    else:
        response = "I'm sorry, I'm not sure how to answer that. Could you please rephrase your question?"


    return response

def identify_question_intent(doc):
  

    # Directly checking the text for greetings before extracting other keywords
    greeting_keywords = ["good morning", "hi", "how are you", "hello", "good afternoon", "good evening"]
    pricing_keywords = ["price", "cost", "quote", "quotation", "rate", "amount", "charge", "fee", "how much"]
    location_keywords = ["location", "where", "region", "area", "place", "site", "spot", "venue", "destination", "address","pickup","dropoff"]
    features_keywords = ["features", "highlights", "activities", "attractions", "amenities", "facilities", "services"]
    duration_keywords = ["duration", "how long", "how much time", "how many hours", "how many days", "how many weeks", "how many months", "how many years"]
    contact_keywords = ["contact", "phone", "email", "address", "contact number", "contact details", "contact information"]
    website_keywords = ["website", "link", "webpage", "webpage", "web address", "URL", "web link", "web site"]
    time_keywords = ["time", "reporting","hour"]

    doc_text = doc.text.lower()  # Get the full text of the user input in lowercase
    if any(greeting in doc_text for greeting in greeting_keywords):
        question_intent="greetings"
    elif any(pricing_keyword in doc_text for pricing_keyword in pricing_keywords):
        question_intent="price_inquiry"
    elif any(location_keyword in doc_text for location_keyword in location_keywords):
        question_intent="location_inquiry"
    elif any(features_keyword in doc_text for features_keyword in features_keywords):
        question_intent="features_inquiry"
    elif any(duration_keyword in doc_text for duration_keyword in duration_keywords):
        question_intent="duration_inquiry"
    elif any(contact_keyword in doc_text for contact_keyword in contact_keywords):
        question_intent= "contact_inquiry"
    elif any(website_keyword in doc_text for website_keyword in website_keywords):
        question_intent="website_inquiry"
    elif any(time_keyword in doc_text for time_keyword in time_keywords):
        question_intent="time_inquiry"
    else:
        question_intent="other"
    
    return question_intent
    
    
    
    # # else:
    # #     return "other"

    # # Continue with the rest of the function if no greeting is detected
    # # keywords = [token.text.lower() for token in doc if token.pos_ in ["NOUN", "PROPN", "INTJ"]]
    # # entities = doc.ents

    # # question_intent = None # Default to "other"
    # # Your existing conditions for identifying other intents
    # # ...

    # # return question_intent


    # # keywords = [token.text.lower() for token in doc if token.pos_ in ["NOUN", "PROPN"]]
    # # entities = doc.ents

    # # Simple rule-based matching example:
    # # question_intent = None
    # # if any(word in keywords for word in ["good morning", "hi", "how are you", "hello", "good afternoon", "good evening"]):
    # #     question_intent="greetings"
    # # elif any(word in keywords for word in ["price", "cost","quote","quotation","rate","amount","charge","fee","how much"]):
    # #     question_intent = "price_inquiry"
    # # elif any(word in keywords for word in ["location", "where"]):
    # #     question_intent = "location_inquiry"
    # # elif any(entity.label_ == "GPE" for entity in entities):  # Check for geographical entities
    # #     question_intent = "location_inquiry"
    # # elif any(word in keywords for word in ["features", "highlights"]):
    # #     question_intent = "features_inquiry"
    # # elif any(word in keywords for word in ["duration", "how long"]):
    # #     question_intent = "duration_inquiry"
    # # elif any(word in keywords for word in ["contact", "phone", "email"]):
    # #     question_intent = "contact_inquiry"
    # # elif any(word in keywords for word in ["website", "link"]):
    # #     question_intent = "website_inquiry" 
    # # elif any(word in keywords for word in ["region", "area"]):
    # #     question_intent = "region_inquiry"
    # # elif any(word in keywords for word in ["good morning", "hi", "how are you","hello", "good afternoon", "good evening"]):
    # #     question_intent = "greetings"
    # # else:
    # #     question_intent = "other"

    # return question_intent

