from pandas import read_csv
from matplotlib.pyplot import *

gender_degree_data = read_csv("percent-bachelors-degrees-women-usa.csv")

figure()

majors = ['Health Professions', 'Public Administration', 'Education', 'Psychology',
          'Foreign Languages', 'English', 'Communications\nand Journalism',
          'Art and Performance', 'Biology', 'Agriculture',
          'Social Sciences and History', 'Business', 'Math and Statistics',
          'Architecture', 'Physical Sciences', 'Computer Science',
          'Engineering']

for rank, column in enumerate(majors):
    plot(gender_degree_data.Year.values,
         gender_degree_data[column.replace("\n", " ")].values,
         lw=2.5)

    y_pos = gender_degree_data[column.replace("\n", " ")].values[-1] - 0.5
    if column == "Foreign Languages":
        y_pos += 0.5
    elif column == "English":
        y_pos -= 0.5
    elif column == "Communications\nand Journalism":
        y_pos += 0.75
    elif column == "Art and Performance":
        y_pos -= 0.25
    elif column == "Agriculture":
        y_pos += 1.25
    elif column == "Social Sciences and History":
        y_pos += 0.25
    elif column == "Business":
        y_pos -= 0.75
    elif column == "Math and Statistics":
        y_pos += 0.75
    elif column == "Architecture":
        y_pos -= 0.75
    elif column == "Computer Science":
        y_pos += 0.75
    elif column == "Engineering":
        y_pos -= 0.25

    text(2011.5, y_pos, column)

text(1995, 93, "Percentage of Bachelor's degrees conferred to women in the U.S.A."
               ", by major (1970-2012)", fontsize=17, ha="center")

text(1966, -8, "Data source: nces.ed.gov/programs/digest/2013menu_tables.asp", fontsize=10)

savefig("percent-bachelors-degrees-women-usa_minimum.png", bbox_inches="tight")