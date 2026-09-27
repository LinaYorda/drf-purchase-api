"""
Curated book titles and a realistic price helper for seed data.

Faker's random-sentence generator produces filler like "Wife car less.",
which doesn't read as a real book title. This file replaces that with
300 plausible titles (a mix of well-known classics and invented-but-
believable ones) and realistic price ranges. See AGENTS.md.
"""

import random

BOOK_TITLES = [
    # Classics / widely recognizable (70)
    "Pride and Prejudice", "1984", "Moby-Dick", "The Great Gatsby",
    "War and Peace", "Crime and Punishment", "To Kill a Mockingbird",
    "Brave New World", "The Catcher in the Rye", "Jane Eyre",
    "Wuthering Heights", "Anna Karenina", "The Odyssey", "Don Quixote",
    "Frankenstein", "Dracula", "The Picture of Dorian Gray",
    "A Tale of Two Cities", "Great Expectations", "Les Misérables",
    "The Brothers Karamazov", "One Hundred Years of Solitude",
    "The Grapes of Wrath", "Slaughterhouse-Five", "Fahrenheit 451",
    "The Old Man and the Sea", "Of Mice and Men", "Lord of the Flies",
    "The Metamorphosis", "The Stranger", "Heart of Darkness",
    "Madame Bovary", "The Sound and the Fury", "As I Lay Dying",
    "Middlemarch", "Vanity Fair", "The Count of Monte Cristo",
    "The Three Musketeers", "Robinson Crusoe", "Gulliver's Travels",
    "The Scarlet Letter", "Little Women", "The Adventures of Huckleberry Finn",
    "The Adventures of Tom Sawyer", "Treasure Island", "The Secret Garden",
    "Alice's Adventures in Wonderland", "Through the Looking-Glass",
    "Peter Pan", "The Wind in the Willows", "Animal Farm", "The Trial",
    "The Idiot", "Demons", "Siddhartha", "The Alchemist", "Norwegian Wood",
    "Kafka on the Shore", "Beloved", "Invisible Man", "Native Son",
    "The Color Purple", "A Room with a View", "Howards End",
    "The Age of Innocence", "Ethan Frome", "My Ántonia", "O Pioneers!",
    "The House of Mirth",

    # Mystery / thriller (50)
    "The Silent Correspondent", "A Quiet Kind of Disappearance",
    "The Last Ferry to Blackpool", "Nine Doors, One Exit",
    "The Cartographer's Secret", "What the Tide Left Behind",
    "The Widow of Cedar Street", "A Study in Ashes",
    "The Locksmith's Daughter", "Shadows Over Millbrook",
    "The Witness Who Wasn't There", "Ink and Alibi", "The Vanishing Hour",
    "Three Letters, No Return Address", "The Glasshouse Murders",
    "A Cold Case in Amber", "The Detective's Last Confession",
    "Six Suspects, One Storm", "The Man in Compartment Nine",
    "A Whisper Down Fenwick Lane", "The Inspector's Quiet War",
    "Blood on the Ledger", "The Undertaker's Alibi",
    "A Death at Windmere Hall", "The Silent Partner's Confession",
    "Midnight at the Aldgate Exchange", "The Forger's Last Canvas",
    "A Trail of Cold Coffee", "The Vanishing of Nora Hale",
    "Seven Days Before the Verdict", "The Reluctant Witness",
    "A Murder in Three Acts", "The Clockwork Alibi",
    "Deadline at the Harbor Press", "The Case of the Missing Hours",
    "A Quiet Word with the Coroner", "The Embezzler's Daughter",
    "Smoke and Circumstance", "The Night the Lighthouse Went Dark",
    "A Confession in Longhand", "The Pawnbroker's Last Client",
    "Ten Minutes Past the Alibi", "The Unmarked Grave at Kestrel Farm",
    "A Case of Borrowed Names", "The Informant's Silence",
    "Murder on the Overnight Express", "The Last Client of the Day",
    "A Verdict Written in Smoke", "The Housekeeper Knew Everything",
    "The Detective Who Retired Too Soon",

    # Science fiction / fantasy (50)
    "The Drowned Stars", "Children of the Second Sun",
    "The Clockmaker's Rebellion", "Ashes of the Ninth Colony",
    "The Long Dark Between Worlds", "Wolves of the Iron Kingdom",
    "The Last Cartographer of Mars", "Kingdom of Glass and Smoke",
    "The Silence Between Stars", "Beyond the Salt Horizon",
    "The Bone Orchard", "A Crown of Frost and Fire",
    "The Machine That Dreamed", "Voyage of the Restless Tide",
    "The Whispering Archive", "Empire of Falling Leaves",
    "The Starless Armada", "Daughters of the Iron Moon",
    "The Last Signal from Kepler Station", "A Throne Carved From Ice",
    "The Clockwork Heart of Varn", "Beneath the Copper Sky",
    "The Wanderer's Compass", "Children of the Drowned City",
    "The Emberwood Chronicles", "A Storm of Glass Wings",
    "The Forgotten Colony of Thessaly", "Wolves at the Gate of Dawn",
    "The Cartographer of Lost Realms", "A Rebellion of Small Machines",
    "The Last Garden on Mars", "Kingdom of the Quiet Flame",
    "The Exile of Varengard", "A Thousand Suns Over Karth",
    "The Keeper of the Ninth Gate", "Children of the Broken Moon",
    "The Alchemist's Rebellion", "A Voyage Through Borrowed Time",
    "The Last City Beneath the Ice", "Empire of the Falling Stars",
    "The Clockwork Prophecy", "A Kingdom Built on Ashes",
    "The Silent Fleet of Orin", "Daughters of the Storm King",
    "The Forgotten Frequency", "A Throne of Salt and Starlight",
    "The Wanderers of Nightfall Station", "Children of the Iron Tide",
    "The Last Lighthouse in the Dark Sea", "A Rebellion Written in Starlight",

    # Romance (30)
    "Meet Me at the Blue Hour", "The Orchard We Never Sold",
    "Letters from a Quiet Summer", "Somewhere Near Enough",
    "The Bookshop on Lantern Street", "Autumn in Two Voices",
    "A Promise Written in Rain", "The Year of Small Beginnings",
    "Every Sunday in Provence", "The Café at the End of Marlowe Street",
    "A Season of Borrowed Umbrellas", "Two Trains to Somewhere Better",
    "The Postcard from Amalfi", "Falling for the Quiet Season",
    "A Letter Never Sent to Rome", "The Winter We Almost Stayed",
    "Somewhere Between Dublin and Dusk", "The Last Dance at Willowmere",
    "A Summer of Borrowed Bicycles", "The Orchard at Hollyhock Lane",
    "Two Strangers on the Night Train", "The Garden We Almost Forgot",
    "A Quiet Kind of Falling", "The Letters We Kept",
    "Somewhere South of Ordinary", "The Year We Almost Left",
    "A Promise at the Ferry Dock", "The Bookshop Where We Met",
    "Autumn Somewhere Else", "The Quiet Arithmetic of Us",

    # Non-fiction (35)
    "Sapiens: A Brief History of Humankind", "Atomic Habits",
    "Thinking, Fast and Slow", "Quiet: The Power of Introverts",
    "Deep Work", "The Psychology of Money",
    "A Short History of Nearly Everything", "The Warmth of Other Suns",
    "Educated: A Memoir", "The Body Keeps the Score",
    "Man's Search for Meaning", "The Elegant Universe",
    "Outliers: The Story of Success", "The Power of Habit",
    "Guns, Germs, and Steel", "The Righteous Mind",
    "Blink: The Power of Thinking Without Thinking", "Freakonomics",
    "The Tipping Point", "Into the Wild", "The Art of Slow Thinking",
    "The Undoing of Us", "How to Talk to Absolutely Anyone",
    "The Ten-Minute Discipline", "The Practice of Deep Attention",
    "A Short History of Wasted Time", "The Economics of Everyday Kindness",
    "Notes on Doing Less", "The Discipline of Small Decisions",
    "A Field Guide to Difficult Conversations",
    "The Grammar of Getting Things Done",
    "Everything I Learned From Waiting Rooms", "The Quiet Science of Habits",
    "A Short Course in Paying Attention", "The Geography of Second Chances",

    # General fiction (65)
    "The Last Light in Marlow", "Everything We Buried in June",
    "The Weight of Small Rooms", "Three Winters in Odense",
    "The Gardener's Apprentice", "A House Made of Rumor",
    "The Cartwright Inheritance", "Notes from the Northbound Train",
    "The Quiet Machinery of Grief", "Salt and Marrow",
    "The Year the River Rose", "Everyone Who Left Before Us",
    "The Longest Shortcut Home", "A Field Guide to Losing Things",
    "The Unsent Postcards", "What the Orchard Remembers",
    "The Paper Lantern District", "The Almanac of Ordinary Days",
    "Songs for the Empty House", "The Keeper of Small Debts",
    "Rooms We Used to Live In", "The Cartography of Regret",
    "A Thousand Ordinary Mornings", "The Last Bookshop in Hallow's End",
    "Everything Left Unsaid at Dover", "The Clockwork Orchard",
    "A Map of Quiet Places", "The Weaver's Daughter",
    "Letters to No One in Particular", "The Season We Stopped Counting",
    "The Hourglass Keeper", "Where the Wildflowers Winter",
    "The Uninvited Guest at Thornwood", "A Brief History of Almost Everyone",
    "The Lighthouse Keeper's Ledger", "Notes on a Vanishing Coastline",
    "The Farmhouse at the End of April", "Everything the Storm Carried",
    "The Quiet Ones of Ashbury", "A Catalogue of Small Regrets",
    "The Ferryman's Last Crossing", "Between Two Winters",
    "The Alchemist's Grandson", "A Hundred Small Kindnesses",
    "The Orphaned Library", "What Remains at Willow Creek",
    "The Traveler's Almanac", "A Season of Borrowed Time",
    "The Cottage on Harrow Lane", "Everything We Never Mailed",
    "The Bookbinder of Prague", "A Quiet Rebellion",
    "The Midnight Cartographer", "Letters from the Far Shore",
    "The Last Harvest at Bellwood", "A Small, Stubborn Light",
    "The Chronicle of Ordinary Things", "Where the Foxes Winter",
    "The Innkeeper's Daughter", "A Dictionary of Lost Words",
    "The Wandering Bookseller", "Notes from a Northern Winter",
    "The Reluctant Astronomer", "A Field of Quiet Fires",
    "The Season Before the Frost", "The Last Letter from Avondale",
]


def random_book_title():
    return random.choice(BOOK_TITLES)


def realistic_price():
    """A single book's realistic retail price."""
    return round(random.uniform(8.99, 45.99), 2)


def realistic_purchase_price():
    """A whole purchase can contain multiple books, so allow a wider range."""
    return round(random.uniform(8.99, 120.00), 2)
