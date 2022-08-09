# ScoutingDIVE

A scouting data validation system built on [PWNAGE 2451's Scouting P.A.S.S.](https://github.com/PWNAGERobotics/ScoutingPASS)

## Features:

### **Configurable**

- Adjustable for any scouting app/Excel workbook
- Uses convenient and accessible pandas to read Excel data and requests to read TBA data

### **User-Friendly**

- Written in Python - easy to download and understand

### **[The Blue Alliance](https://www.thebluealliance.com) Integration**

- Automatically pulls match data from TBA
- Makes for quick and easy data comparison

## About ScoutingDIVE:

ScoutingDIVE stands for Scouting Data and Information Validation Effort. Its goal is to provide a simple, quick, and easy way to compare FRC scouting data with official match scores. By using ScoutingDIVE, students and mentors can assess and improve their scouting data and techniques.

ScoutingDIVE takes user input (event year, code, and match number) and collects the match score from the TBA API. From there, it compares both the scouter-generated match score with the official final score. Scouting P.A.S.S. does not automatically track fouls, so ScoutingDIVE also adds foul points from TBA to the scouter-generated match score for comparison purposes.

ScoutingDIVE also tracks the amount of error in your scouting data. After reading, tabulating, and printing match scores, ScoutingDIVE prints whether the scouter-generated score (with fouls) is within 5% of the official score. 

ScoutingDIVE was designed for all users, especially those with minimal programming experience - a majority of the ScoutingDIVE setup is done in Excel rather than Python. 

ScoutingDIVE is usable from year to year, as its setup is not based on a specific FRC game - just on what is in your Excel workbook.


## Getting Started:

- Fork GitHub project
- Download Python and install pandas and requests
- Add your TBA auth key and scouting datasheet filepath to their respective variables
- Adjust spreadsheet rows/columns as needed to match your data

Check out [spreadsheetsetup.md](main/spreadsheetsetup.md) to see how Scouting P.A.S.S.'s Excel workbook integrates with ScoutingDIVE!


## Future Updates:

- UI improvements
- Graphing of scouting data vs. TBA data
- Pulling match numbers/lists from TBA (instead of spreadsheet)
- Support for playoff match data (currently only qualification match data is accessible)


## Contributing:

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion for improving ScoutingDIVE, fork the repo and make a pull request. You can also open an issue to state what you'd like changed.

Don't forget to give this project a star!


## License:

Distributed under the GNU GPL v3.0 License.

