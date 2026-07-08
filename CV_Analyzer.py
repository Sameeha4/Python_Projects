import json
import os
from ollama import chat
from pypdf import PdfReader
print("=================================\n    AI Resume Analyzer    \n=================================")
while True:
   while True:
      resume_file=input("ENTER RESUME FILE NAME IT MUST BE IN .PDF EXTENSION=")
      if os.path.exists(resume_file):
            name, ext = os.path.splitext(resume_file)
            if ext.lower() != ".pdf":
               print("Invalid file type. Please provide a PDF file")
               continue
      else:
            print("not found \nPlease enter correct file Name")
            continue
      break
   while True:
      description_file=input("ENTER JOB_DESCRIPTION FILE NAME IT MUST BE IN .TXT EXTENSION=")
      if os.path.exists(description_file):
            name, ext = os.path.splitext(description_file)
            if ext.lower() != ".txt":
                  print("Invalid file type. Please provide a txt file")
                  continue
      else:
            print("not found\nPlease enter correct file Name")
            continue
      break
   try:
        reader = PdfReader (resume_file)
        pages = reader.pages
   except:
        print("Unable to read the PDF file.\nThe file may be corrupted, encrypted, or not a valid PDF.\nPlease select another file.")
        continue
   try:
        with open(description_file,"r") as f:
         description=f.read()
   except:
        print("Unable to read the txt file.\nThe file may be corrupted, encrypted, or not a valid PDF.\nPlease select another file.")
        continue
   resume_text=str()
   print("ANlYZEING YOUR RESUME..")
   for i in pages:
      page_text=i.extract_text()
      if page_text is None:
           print("Page",i,"extract nothing")
      else:
           resume_text+=page_text
   if  resume_text=="":
      print("YOUR UPLOADED RESUME FILE CONTAINS UNEXTRACTABLE TEXT \nPLEASE ENTER VALID FILE")
      continue
   break
messages=[]
messages.append({
   "role": "system",
   "content":
   " Role:\n"
   "You are an ATS Resume Analyzer.\n" 
   "Your task:\n"
   "Analyze the resume against the job description\n"
   "Provide concise and actionable answers.\n"
   "Do not add explanations before or after JSON.Return only valid JSON.\n"
   "Required fields:\n"
   "- summary\n"
   "- match_score\n"
   "- matching_skills\n"
   "- missing_skills\n"
   "- strengths\n"
   "- weaknesses\n"
   "- recommendation\n"
   "Job Description:\n"
      + description +
   "\n\nResume:\n"
      + resume_text 
})
print("Thanks for providing both files.\n===============\n  AI REPORT  \n===============")
response=chat(
   model="qwen2.5:3b",
   messages=messages
)
bot_response=response.message.content
report = json.loads(bot_response)
print("Summary:")
print(report["summary"])
print("Match Score:")
print(report["match_score"])
print("Matching Skills:")
for skill in report["matching_skills"]:
   print("-", skill)
print("Missing Skills:")
for skill in report["missing_skills"]:
   print("-", skill)
print("Strengths:")
for skill in (report["strengths"]):
   print("-", skill)
print("Weaknesses:")
for skill in (report["weaknesses"]):
   print("-",skill)
print("Recommendations")
print(report["recommendation"])
messages.append({
    "role": "system",
    "content":
    "You are an AI Career Counselor and Resume Advisor.\n"
    "Use the provided resume and job description as context.\n"
    "Answer the user's questions about their resume, skills, career growth, interview readiness, and job fit.\n"
    "Provide concise, practical, and actionable advice.\n"
    "Do not return JSON unless explicitly requested.\n"
})
while True:
   print(".Would you like to ask something?\n.Exit\nYOU:",end="")
   user_input=input("")
   if user_input.lower()=="exit":
      print("THANKS FOR USE MY APP!")
      break
   messages.append(
   {
   "role":"user",
   "content":user_input
   })
   response=chat(
   model="qwen2.5:3b",
   messages=messages
   )
   bot_response=response.message.content
   print("ASSISTANT:",bot_response)
   messages.append({
   "role":"assistant",
   "content":bot_response
   })
