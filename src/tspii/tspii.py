import os
from tspii.reversible_anonymizers.reversible_anonymizer import ReversibleAnonymizer
from tspii.recognizers.recognizers import create_travel_specific_recognizers
from tspii.operators.faker_operators import create_fake_data_operators


def create_text():
    return """
        Subject: Meeting Details and Updates

        Dear Team,

        I hope this message finds you well today. I wanted to share a few updates regarding the upcoming project kickoff meeting, which is scheduled for April 12, 2025, at 3:00 PM EST. Below, you’ll find the key details for the meeting.

        The attendees will include a Senior Software Engineer from Tech Innovations Inc. (John S.) and a Marketing Manager from Creative Designs Ltd. (Maria G.).

        The agenda for the meeting will cover an introduction to the new project, a review of deliverables and the timeline, and a Q&A session. Additionally, one of the attendees will be traveling from New York to London on April 15, 2025, for a client presentation.

        For those involved with the project budget approval, the financial details include the SWIFT Code ABCDUS33, GB29NWBK60161331926819, and 021000021.

        Please confirm your attendance by March 30, 2025, and feel free to reach out if you have any concerns.

        Best regards,
        Anna P.
        Project Manager, Tech Innovations Inc.
    """


def load_document_from_file(file_path):
    """Function to load document content from a text file"""
    try:
        with open(file_path, "r") as file:
            document_content = file.read()
        return document_content
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None


def save_pseudonymized_content_to_file(file_path, content):
    """Function to save pseudonymized content to a text file"""
    with open(file_path, "w") as file:
        file.write(content)
    print(f"pseudonymized content saved to {file_path}")


def pseudonymize_text(text):
    """Sample function to handle the pseudonymization process"""
    reversible_anonymizer = ReversibleAnonymizer()

    # Add recognizers
    for recognizer in create_travel_specific_recognizers():
        reversible_anonymizer.add_recognizer(recognizer)

    # Add operators
    reversible_anonymizer.add_operators(create_fake_data_operators())

    # Analyze the text
    reversible_anonymizer.analyze(text)

    # Anonymize the text
    result = reversible_anonymizer.anonymize()

    return result.text


def main():

    # Option for user to either load document from file or use sample
    print("Welcome to the Document pseudonymizer.")
    choice = input(
        "Would you like to (1) Load a document from a file or (2) Use the sample document? Enter 1 or 2: "
    )

    if choice == "1":
        file_path = input("Enter the path to the text file: ")
        document_content = load_document_from_file(file_path)
        if document_content:
            pseudonymized_content = pseudonymize_text(document_content)
            print(f"Result of the pseudonymization:\n{pseudonymized_content}")

            save_option = input(
                "Would you like to save the pseudonymized document? (y/n): "
            )
            if save_option.lower() == "y":
                save_path = input(
                    "Enter the path to save the pseudonymized content (e.g., pseudonymized_document.txt): "
                )
                save_pseudonymized_content_to_file(save_path, pseudonymized_content)

    elif choice == "2":
        # Run the process on the sample document
        pseudonymized_content = pseudonymize_text(create_text())
        print(f"Result of the pseudonymization:\n{pseudonymized_content}")

        save_option = input(
            "Would you like to save the pseudonymized document? (y/n): "
        )
        if save_option.lower() == "y":
            save_path = input(
                "Enter the path to save the pseudonymized content (e.g., pseudonymized_document.txt): "
            )
            save_pseudonymized_content_to_file(save_path, pseudonymized_content)
    else:
        print("Invalid choice. Please run the program again and select a valid option.")


main()
