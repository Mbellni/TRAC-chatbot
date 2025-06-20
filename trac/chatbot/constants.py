from colorama import Fore, Style

# === General UI Strings ===
RETRY_YES_NO = f"""{Fore.GREEN}
Apologies but I did not understand. [[pause=1]]
Please type either 'yes' or 'no'.
{Style.RESET_ALL}"""
RETRY_YES_SKIP = f"""{Fore.GREEN}
Apologies but I did not understand. [[pause=1]]
Please type 'yes' or 'skip'.
{Style.RESET_ALL}"""
RETRY_START = f"""{Fore.GREEN}
Apologies but I did not understand. [[pause=1]]
Please type 'start' when you're ready to begin the exercise.
{Style.RESET_ALL}"""
RETRY_START_SKIP = f"""{Fore.GREEN}
Apologies but I did not understand. [[pause=1]]
Please type either 'start' or 'skip'.
{Style.RESET_ALL}"""
RETRY_CONTINUE = f"""{Fore.GREEN}
Apologies but I did not understand. [[pause=1]]
Please type 'continue' when you’re ready to move on.
{Style.RESET_ALL}"""
RETRY_CAFE_PROMPT = f"""{Fore.GREEN}
Apologies but I did not understand. [[pause=1]]
Please type either "yes" or "conclude."
{Style.RESET_ALL}"""
RETRY_AFFIRMATION_CHOICE = f"""{Fore.GREEN}
Apologies but I did not understand. [[pause=1]]
Please type '1', '2', '3' or '4'.
{Style.RESET_ALL}"""

# === Intro ===
INTRO_TEXT = f"""{Fore.GREEN}
Hello, I’m TRAC, your Tranquility, Reflection 
and Awareness Chatbot. [[pause=2]]

I’m here to help you find moments of calm and clarity. [[pause=2]]

Whether you’re feeling overwhelmed or just need to 
unwind a bit, these strategies can be a great way to 
restore balance. [[pause=3]]
{Style.RESET_ALL}"""
QUESTION_START = f"""{Fore.GREEN}
Shall we get started? 
Please type 'yes' or 'no'.
{Style.RESET_ALL}"""
EXIT_MESSAGE = f"""{Fore.GREEN}
That is alright. [[pause=1]] 
If you change your mind and 
want to give in to relaxation, I am a push of 
a button away. [[pause=1]] Hope to see you soon.
{Style.RESET_ALL}"""

# === Breathing ===
BREATHING_INTRO = f"""{Fore.GREEN}
Would you like to try a breathing exercise, 
or perhaps explore a different calming approach 
that feels right for you? [[pause=4]]

Note: Please don’t attempt this exercise if you 
have breathing problems or any conditions that 
may worsen by this exercise. [[pause=4]]
{Style.RESET_ALL}"""
QUESTION_BREATHING_1 = f"""{Fore.GREEN}
Shall we get started?
Please type "yes" or "skip".
{Style.RESET_ALL}"""
POSITIVE_ACK = f"{Fore.GREEN}Wonderful!{Style.RESET_ALL}\n"
BREATHING_DETAILS = f"""{Fore.GREEN}
Let’s do the 4-4-4 exercise. [[pause=2]]

You’re going to take a deep breath in for 4 counts, 
hold for 4 counts and exhale for 4 counts. [[pause=3]]

I will take care of the counts so you can just sit back and relax. [[pause=3]]
{Style.RESET_ALL}"""
QUESTION_BREATHING_START = f"""{Fore.GREEN}
Do you wish to start? 
Type 'start' when you are ready.
{Style.RESET_ALL}"""
AFTER_BREATHING_MSG = f"""{Fore.GREEN}
Well done! [[pause=1]] 
Breathing can be a great way to bring focus to 
the body while emptying your mind. [[pause=3]]
{Style.RESET_ALL}"""
QUESTION_FEELING_AFTER_BREATHING = f"""{Fore.GREEN}How are you feeling right now?{Style.RESET_ALL}"""
REPEAT_BREATHING_PROMPT = f"""{Fore.GREEN}
If you'd like, we can try the breathing exercise again 
to help bring you some calm. [[pause=3]]
{Style.RESET_ALL}"""
REPEAT_BREATHING_Q = f"{Fore.GREEN}Would you be interested?{Style.RESET_ALL}"
ACK_NO_REPEAT = f"{Fore.GREEN}That's perfectly ok! [[pause=1]]{Style.RESET_ALL}"
RESPONSES_SENTIMENT = {
    "negative": f"{Fore.GREEN}It's okay to feel this way, and it will get better. [[pause=2]]{Style.RESET_ALL}",
    "neutral": f"{Fore.GREEN}Got it.[[pause=1]] Thank you for sharing that with me. [[pause=2]]{Style.RESET_ALL}",
    "positive": f"{Fore.GREEN}It’s great that you’re feeling good! [[pause=2]]{Style.RESET_ALL}",
    "default": f"{Fore.GREEN}Hmm, feelings can be confusing... [[pause=2]]{Style.RESET_ALL}"
}

# === Grounding ===
GROUNDING_INTRO = f"""{Fore.GREEN}
Let’s try something a bit different instead. [[pause=2]]
We’ll move on to a grounding exercise that can 
help bring you into the present moment and find 
a sense of calm. [[pause=4]]

There is no pressure! You will have time to finish 
the exercise before moving on. If you feel more 
comfortable, wait until I finish naming all the steps. [[pause=5]]
{Style.RESET_ALL}"""
GROUNDING_PROMPT = f"{Fore.GREEN}Please type 'start' or 'skip'.\n{Style.RESET_ALL}"
GROUNDING_EXERCISE = f"""{Fore.GREEN}
Let’s try a grounding exercise called “5-4-3-2-1.” [[pause=3]]
This helps bring you to the present moment. [[pause=3]]

- Name **5 things** you can see around you. [[pause=3]]

- Name **4 things** you can touch. [[pause=3]]

- Name **3 things** you can hear. [[pause=3]]

- Name **2 things** you can smell. [[pause=3]]

- And finally, name **1 thing** you can taste. [[pause=3]]
{Style.RESET_ALL}"""

# === Continue Prompt ===
CONTINUE_PROMPT = f"""{Fore.GREEN}
Take your time and let me know when you're ready
 to continue.
 
Please type "continue".
{Style.RESET_ALL}"""
CONTINUE_ACK = f"""{Fore.GREEN}
Well done! [[pause=1]] 
Taking a moment to ground yourself 
can be so powerful. [[pause=2]]
{Style.RESET_ALL}"""

# === Affirmations ===
POSITIVE_INTRO = f"""{Fore.GREEN}
Now, let’s continue with some positive affirmations 
to uplift and encourage you. These can be a wonderful 
way to reinforce a sense of confidence. [[pause=5]]
{Style.RESET_ALL}"""
AFFIRMATIONS_START_PROMPT = f"""{Fore.GREEN}
Ready to give it a try? [[pause=1]] 
Please type "start" or "skip".
{Style.RESET_ALL}"""
AFFIRMATIONS_LIST = f"""{Fore.GREEN}
Here are a few affirmations for today. Repeat each one 
slowly to yourself, or let me know which resonates most: [[pause=4]]

1 - “I am worthy of peace and calm.” [[pause=2]]

2 - “I am doing my best, and that’s enough.” [[pause=2]]

3 - “I am resilient, strong, and capable.” [[pause=2]]

4 - “I trust myself to handle what comes my way.” [[pause=3]]
{Style.RESET_ALL}"""
AFFIRMATION_CHOICE_PROMPT = f"{Fore.GREEN}Which one speaks to you most? Phrase 1, 2, 3 or 4?{Style.RESET_ALL}"
AFFIRMATION_RESPONSES = {
"1": f"""{Fore.GREEN}
Absolutely, you deserve all the peace and calm 
that life has to offer. [[pause=3]] Embracing that worthiness 
can be so empowering. [[pause=2]]
{Style.RESET_ALL}""",
"2": f"""{Fore.GREEN}
That’s a beautiful reminder. [[pause=2]] Your best is more 
than enough, and honoring that can bring such 
a sense of relief. [[pause=3]]
{Style.RESET_ALL}""",
"3": f"""{Fore.GREEN}
Yes! [[pause=1]] You have such strength within you. [[pause=2]] 
Remembering this can help you face any challenge 
that comes your way. [[pause=3]]
{Style.RESET_ALL}""",
"4": f"""{Fore.GREEN}
Trusting yourself is so powerful. [[pause=2]] You’re capable and 
resilient, ready to face whatever comes. [[pause=3]]
{Style.RESET_ALL}"""
}
POSITIVE_REINFORCEMENT = f"""{Fore.GREEN}
Great job! [[pause=1]] Taking a moment to connect with yourself 
like this is a wonderful step. [[pause=3]]
{Style.RESET_ALL}"""
CAFE_INTRO = f"""{Fore.GREEN}
Now that we’ve set a positive foundation, let’s 
explore some cozy cafes where you can relax, 
reflect, or simply enjoy a peaceful moment. [[pause=5]]
{Style.RESET_ALL}"""
CAFE_PRIVACY_NOTE = f"""{Fore.GREEN}
Quick note: our cafe recommendations use a 
location-based search to find calming spots 
nearby, but rest assured, your location 
information is only used temporarily for this 
purpose and isn’t stored. [[pause=8]] 

Your privacy and confidentiality are always protected. [[pause=2]] 

Also, this task requires wifi connection. [[pause=2]]{Style.RESET_ALL}"""

# === Cafe Flow ===
CAFE_PROMPT = f"""{Fore.GREEN}
Ready to find a cozy spot? 
Please type "yes" or "conclude".
{Style.RESET_ALL}"""
CAFE_FOUND = f"{Fore.GREEN}I hope you found a cafe that piqued your interest! [[pause=2]]{Style.RESET_ALL}"
CAFE_NOT_FOUND = f"{Fore.GREEN}I'm sorry I couldn't find any cafes nearby. [[pause=2]]{Style.RESET_ALL}"
CAFE_CONCLUDE_TEXT = f"""{Fore.GREEN}
Thank you for spending this time with me today. [[pause=2]]

I hope the techniques we explored bring you some calm and comfort. [[pause=3]]
{Style.RESET_ALL}"""

# === Cafe Logic ===
ENTER_POSTAL_CODE = f"{Fore.GREEN}Please enter your postal code: {Style.RESET_ALL}"
ENTER_RADIUS = f"{Fore.GREEN}Enter the search radius in miles (numbers only): {Style.RESET_ALL}"
INVALID_RADIUS_INPUT = f"{Fore.GREEN}Invalid input for radius. Please enter a valid number.{Style.RESET_ALL}"
INVALID_POSTAL_CODE = f"{Fore.GREEN}Invalid postal code. Please try again.{Style.RESET_ALL}"
LOCATION_NOT_FOUND = f"{Fore.GREEN}Could not find location for postal code: {{}}{Style.RESET_ALL}"
LOCATION_ERROR = f"{Fore.GREEN}Error occurred while fetching location: {{}}{Style.RESET_ALL}"
NO_CAFES_IN_RADIUS = f"{Fore.GREEN}No nearby cafes found within the given radius.{Style.RESET_ALL}"
CAFES_WITHIN_RADIUS = f"{Fore.GREEN}Nearby cafes within {{}} miles (max {{}} results):{Style.RESET_ALL}"
CAFE_INFO = f"{Fore.GREEN}{{}} ({{:.2f}} miles){Style.RESET_ALL}"
NO_NAMED_CAFES = f"{Fore.GREEN}No cafes with a name found in the given radius.{Style.RESET_ALL}"
CAFE_FETCH_ERROR = f"{Fore.GREEN}Error: Unable to fetch nearby cafes. Details: {{}}{Style.RESET_ALL}"

# === Conclusion ===
CONCLUSION_PROMPT = f"""{Fore.GREEN}
Before we wrap up, I’d love to hear—
how are you feeling after our session?
{Style.RESET_ALL}"""
CONCLUSION_GENERIC_RESPONSE = f"{Fore.GREEN}It sounds like there’s a lot on your mind. [[pause=2]]{Style.RESET_ALL}"
CLOSING_RECOMMENDATIONS = f"""{Fore.GREEN}
Before we part, here are a few small ways to carry calm 
with you throughout the day: [[pause=5]]

- Pause for a few deep breaths whenever things feel 
overwhelming. Even a moment can help ground you. [[pause=5]]

- Take a brief walk outside or find a quiet corner to 
unwind, especially if you’re feeling a bit unsettled. [[pause=5]]

- Practice gratitude by naming one thing you’re thankful 
for today. It can bring a surprising amount of peace. [[pause=5]]

Remember, it’s okay to take breaks and prioritize your 
well-being. Little moments of care make a big 
difference. [[pause=6]]
{Style.RESET_ALL}"""
FINAL_GOODBYE = f"""{Fore.GREEN}
Thank you for being here, and remember, I’m always just a 
message away if you need a moment of calm. [[pause=5]]
{Style.RESET_ALL}"""
