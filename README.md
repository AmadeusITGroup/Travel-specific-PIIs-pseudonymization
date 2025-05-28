# TravelSpecificPIIPseudonymization

**TravelSpecificPIIPseudonymization** is a Python-based tool designed to detect and pseudonymize personally identifiable information (PII) in travel-related documents. It leverages custom recognizers and fake data generators for specific aviation industry entities such as Passenger Name Records (PNRs), e-tickets, flight numbers, airline and aircraft codes, and airport codes. The pseudonymization tool ensures the privacy and confidentiality of sensitive data commonly found in aviation documents, making it suitable for airline companies, travel agencies, and other organizations dealing with flight information.

## Features

- **Pseudonymization of Travel-Related PII**: Detects and pseudonymizes common entities in airline and aviation-related documents such as:
  - Passenger Name Records (PNRs)
  - E-tickets
  - Aircraft registration numbers
  - IATA/ICAO aircraft and airline codes
  - IATA/ICAO/FAA airport codes
  - Contact information (phone numbers, email addresses)
  
- **Custom Recognizers**: Includes custom patterns to detect industry-specific codes such as flight numbers, e-ticket prefixes, and more.

- **Faker Integration**: Replaces sensitive data with synthetic data using the Faker library, while also providing flexibility for adding custom fake data generators (e.g., generating fake PNRs, e-tickets).

- **Reversible Pseudonymization**: The tool provides mapping between the original and pseudonymized data, allowing for reversible pseudonymization when required (useful for testing or regulatory purposes).



### Components Overview:

1. **`tspii.py`**: This file is the main entry point for the project. It handles document input, pseudonymization execution, and saving the pseudonymized document to a file. You can customize the (de)pseudonymization of your documents by using the `ReversibleAnonymizer` class.

2. **`reversible_anonymizers`**: This directory contains the `ReversibleAnonymizer` core class, that can be used to perform reversible pseudonymization. This class provides methods to (de)anonymize documents, and offers options for customization.

3. **`recognizers`**: Defines custom recognizers to detect specific PII entities in travel-related documents (e.g., PNR, e-tickets, IATA/ICAO codes).

4. **`operators`**: Defines custom operators that will determine the new value of anonymized sentitive data. It implements custom fake data generators that create realistic synthetic data for aviation-related entities (e.g., generating fake PNRs or e-tickets).

5. **`anonymizers`**: Defines a custom method that define the process to anonymize sensitive data.

6. **`deanonymizers`**: Defines a custom method that define the process to deanonymize sensitive data. 

5. **`tests`**: Contains unit tests for the CustomPseudonymizer class, validating the accuracy of the pseudonymization process and ensuring that sensitive information is properly anonymized while maintaining a correct mapping for potential deanonymization.

## Usage

To use the tool, follow these steps:

 ```bash
   pip install travel-pii-anonymisation

   travel_pii

Would you like to (1) Load a document from a file or (2) Use the sample document? Enter 1 or 2:
If you choose 1, you need to specify a file path. (you can use sample.txt in this repository)


```

  
## Minimum Requirements:

Ensure you have at least 1 GB of free storage and a stable internet connection, as this software requires downloading the `en-core-web` package which is approximately 500 MB.

   
## Contributing

Contributions to improve the tool are welcome! Feel free to open issues for bugs or feature requests, or submit pull requests for enhancements.



## Acknowledgements

This project utilizes various libraries, including LangChain for document processing and Presidio for PII detection and anonymization.
