# ChatGPTSQLProject

For this project I created a database of study cards meant to be used to study a deck of cards.

In this project I used MySQL as my database with the following schema:

Decks Table:
<img width="869" alt="Screenshot 2024-10-05 at 12 19 08 AM" src="https://github.com/user-attachments/assets/31ebdd4a-103a-44b1-8908-1e44d2cc4d9f">

Cards Table:
<img width="869" alt="Screenshot 2024-10-05 at 12 19 17 AM" src="https://github.com/user-attachments/assets/c36b5557-b2c6-40c8-ac4a-8546480dbbfb">


In Python, I created a way for me to query the database and ask ChatGPT these 6 questions:
 Question 1: Show me all the cards in the deck titled 'Python Basics'

Question 2: Show me all the cards created by the user'123456789012'

Question 3: Show me all the decks created by the user '123456789012'

Question 4: Show me all the deleted decks

Question 5: Show me all the cards where both the front and back are null

Question 6: Show me all the cards where the back is null

They output these repsonses respectvely:

Question 1:

    Generated SQL Query: SELECT cards.* 
    FROM cards 
    JOIN decks ON cards.deck_id = decks.id 
    WHERE decks.title = 'Python Basics';

    Query Results: [('card001', 'deck001', 'What is a variable?', 'A variable stores data in memory.', '123456789012', '123456789012', datetime.datetime(2024, 10, 4, 22, 16, 48), datetime.datetime(2024, 10, 5, 0, 4, 31)), ('card002', 'deck001', 'What is a loop?', 'A loop repeats a set of instructions.', '123456789012', '123456789012', datetime.datetime(2024, 10, 4, 22, 16, 48), datetime.datetime(2024, 10, 5, 0, 4, 31)), ('card003', 'deck001', 'Front Side is filled in', None, '123456789012', '123456789012', datetime.datetime(2024, 10, 4, 22, 16, 48), datetime.datetime(2024, 10, 5, 0, 9, 21)), ('card004', 'deck001', None, 'Back Side is filled in', '123456789012', '123456789012', datetime.datetime(2024, 10, 4, 22, 16, 48), datetime.datetime(2024, 10, 5, 0, 9, 21)), ('card005', 'deck001', None, None, '123456789012', '123456789012', datetime.datetime(2024, 10, 4, 22, 16, 48), datetime.datetime(2024, 10, 5, 0, 4, 31))]
    
    Friendly Response: The results contain information on five cards, all from the same deck, 'deck001'. The data includes the card's ID, question, answer, two identical number sequences, and timestamps for two related events.
    1. 'card001' asks the question 'What is a variable?' and provides the answer 'A variable stores data in memory.' It was initialized and updated on 4th October 2024.
    2. 'card002' asks 'What is a loop?' and explains that 'A loop repeats a set of instructions.' Both this card and the previous one were updated again on 5th October 2024.
    3. 'card003' has a filled front side but lacks information on the back side. It was also initialized on 4th October 2024 and last updated on the 5th, a bit later than the first two.
    4. For 'card004', the situation is reversed: we have information for the back side, but the front side is empty. The timeline of events for this card parallels that of 'card003'.
    5. Lastly, 'card005' lacks both front and back side information. Like the first two cards, it was last updated early on 5th October 2024.
    The repetitive '123456789012' sequence and the identical initializing timestamps suggest all cards were created in bulk at the same time. Their last update timestamps differ, indicating some cards may have been revised or revisited more recently than others.

Question 2:

    Generated SQL Query: SELECT * FROM cards WHERE created_by = '123456789012';

    Query Results: [('card001', 'deck001', 'What is a variable?', 'A variable stores data in memory.', '123456789012', '123456789012', datetime.datetime(2024, 10, 4, 22, 16, 48), datetime.datetime(2024, 10, 5, 0, 4, 31)), ('card002', 'deck001', 'What is a loop?', 'A loop repeats a set of instructions.', '123456789012', '123456789012', datetime.datetime(2024, 10, 4, 22, 16, 48), datetime.datetime(2024, 10, 5, 0, 4, 31)), ('card003', 'deck001', 'Front Side is filled in', None, '123456789012', '123456789012', datetime.datetime(2024, 10, 4, 22, 16, 48), datetime.datetime(2024, 10, 5, 0, 9, 21)), ('card004', 'deck001', None, 'Back Side is filled in', '123456789012', '123456789012', datetime.datetime(2024, 10, 4, 22, 16, 48), datetime.datetime(2024, 10, 5, 0, 9, 21)), ('card005', 'deck001', None, None, '123456789012', '123456789012', datetime.datetime(2024, 10, 4, 22, 16, 48), datetime.datetime(2024, 10, 5, 0, 4, 31))]

    Friendly Response: These results indicate that there are five cards (card001, card002, card003, card004, and card005) in the deck001. 
    - card001 asks "What is a variable?" and the answer provided is "A variable stores data in memory." This card seems to have been created and modified on October 4, at roughly 10:16 PM and October 5, around 12:04 AM respectively. 
    - card002 asks "What is a loop?" with the answer being "A loop repeats a set of instructions." The creation and modification times are similar to those of card001.
    - card003 only has a front side filled in, with the phrase "Front Side is filled in", and it was last modified at about 12:09 AM on October 5.
    - card004 has only a back side filled in with the text "Back Side is filled in". It shares the same modification time as card003.
    - card005 is currently blank with neither front nor back sides filled in. 
    The same user (with an ID '123456789012') has created and modified all of these cards.

Question 3:

    Generated SQL Query: SELECT * FROM decks WHERE created_by = '123456789012';
    
    Query Results: [('deck001', 'Python Basics', '123456789012', '123456789012', None, datetime.datetime(2024, 10, 4, 22, 16, 44), datetime.datetime(2024, 10, 5, 0, 4, 17)), ('deck002', 'Deleted Deck', '123456789012', '123456789012', datetime.datetime(2024, 10, 4, 22, 16, 45), datetime.datetime(2024, 10, 4, 22, 16, 44), datetime.datetime(2024, 10, 5, 0, 4, 17))]
    
    Friendly Response: The SQL query results show data about two items. 
    The first item is associated with the ID 'deck001'. It is titled 'Python Basics' and is linked to the number '123456789012' twice, perhaps suggesting it has the same creator and owner. The 'Python Basics' deck's data does not include any additional specific attribute as the fifth field is None. It was created on October 4, 2024, at 10:16:44 PM and last updated on October 5, 2024, at 12:04:17 AM.
    The second item with the ID 'deck002' is titled 'Deleted Deck', and similar to the first item, it is also associated with the number '123456789012' twice which might mean that the same person both created and owns it. This item was created on October 4, 2024, at 10:16:45 PM, but interestingly its last update seems to have been performed a second before the creation at 10:16:44 PM. The record was last verified (or interacted with) on October 5, 2024, at 12:04:17 AM.

Question 4:

    Generated SQL Query: SELECT * FROM decks WHERE deleted_at IS NOT NULL;
    
    Query Results: [('deck002', 'Deleted Deck', '123456789012', '123456789012', datetime.datetime(2024, 10, 4, 22, 16, 45), datetime.datetime(2024, 10, 4, 22, 16, 44), datetime.datetime(2024, 10, 5, 0, 4, 17))]
    
    Friendly Response: The query result indicates that there is a deck named "Deleted Deck" with the ID "deck002". This deck has two identification numbers, both are "123456789012". The deck was created on October 4, 2024, at 22:16:44, updated a second later at 22:16:45, and last accessed on October 5, 2024, at 00:04:17.

Question 5:

    Generated SQL Query: SELECT * FROM cards WHERE front_side IS NULL AND back_side IS NULL;
    
    Query Results: [('card005', 'deck001', None, None, '123456789012', '123456789012', datetime.datetime(2024, 10, 4, 22, 16, 48), datetime.datetime(2024, 10, 5, 0, 4, 31))]
   
    Friendly Response: The results from the SQL query indicate that the card labeled "card005" from the deck "deck001" has two numerical identifiers, both being "123456789012". The card seems to have been used or activated twice, once on October 4, 2024, at 10:16:48 PM and then again later on October 5, 2024, at 12:04:31 AM. The fields with "None" values suggest that there might be missing information or the relevant details for those aspects are not available or applicable.

Question 6:

    Generated SQL Query: SELECT * FROM cards WHERE back_side IS NULL;
    
    Query Results: [('card003', 'deck001', 'Front Side is filled in', None, '123456789012', '123456789012', datetime.datetime(2024, 10, 4, 22, 16, 48), datetime.datetime(2024, 10, 5, 0, 9, 21)), ('card005', 'deck001', None, None, '123456789012', '123456789012', datetime.datetime(2024, 10, 4, 22, 16, 48), datetime.datetime(2024, 10, 5, 0, 4, 31))]
    
    Friendly Response: The SQL query results consist of two records related to cards: 'card003' and 'card005'. Both of these cards belong to the same deck, 'deck001'. 
    For 'card003', its status indicates that the front side is filled in. However, no status is provided for 'card005'. Both cards share the same pair of numbers: '123456789012' and the times suggest that they were active on October 4, 2024, and into the early hours of October 5, 2024. 
    'Card003' was last active at 12:09 AM, while 'card005' was last active at 12:04 AM on October 5, 2024.
