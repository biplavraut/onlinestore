"""
Traditional Four Player Nepali card game. 
"""

from distutils.command.build_scripts import first_line_re
from itertools import count
from operator import index
from queue import Empty
from random import shuffle
from subprocess import check_call

## Create a global variable 
outcome_list = ["Has card(s) to defeat", 
        "Doesn't have card to defeat but other of type exists",
         "Does not have the card, has spade(s), must play spade",
          "Can play any card"]

class CardFunctions:
    """ Class that stores different functions. These fucntions should be refered by multiple other classes as needed. """
    def __init__(self) -> None:
        """ tbd """
        pass

    def compare_winner(self, play_card_dict):
        """ This function will compare various cards in a dictionary and retrun the winning player. The dict must have more than one items. The dictionary must be a key:value pair of Player:Card objects"""
        player_list = list(play_card_dict) # Extract the keys (players) from the dictionary and save on the list. This will help access Cards objects or values from the dictionary.  
        current_winning_card = play_card_dict[player_list[0]] # Intitalizing the variable with the first value in the dictionary. This may change depending the values (other cards) in the dict
        current_winning_player = player_list[0] # Initializing the variable with the first key in the dictionary.
        len_dict = len(play_card_dict) # Get length of dictionary for the following for loop to iterage through the cards object. 

        for i in range(len_dict-1):
            challanger_card = play_card_dict[player_list[i+1]] # Next card on the list will be challenging current winner. 
            if current_winning_card.card_type != challanger_card.card_type and challanger_card.card_type != 'Spade': # Scenario where the type of the challanger card is not the same as the current winner. Also, the challengar is not of type "Spade". This card will under no scenario beat the currently winning card on the dictionary.
                i+=1
            elif current_winning_card.card_type == challanger_card.card_type or challanger_card.card_type == 'Spade': # Scenario where the type of the challenger card is the same as the current winning card or the challengar card is Spade, compare the card number to get the winning card. 
                if challanger_card.card_number > current_winning_card.card_number: # If the card number of the challanger card is greater than the current winning card's card number, challanger card will be the current winner in the hand.
                    current_winning_card = challanger_card
                    current_winning_player = player_list[i+1]
        return current_winning_player

    def compare_cards_by_type(self, player, card):
        """ Compare cards by specific type. This function requires a Player object and a Card object. The objective is to
        go compare the card type and weather the player has the card of that specific type in the hand. Also, this function retruns if card of greater value exists or not.  """
        # outcome_list = ["Has card(s) to defeat", 
        # "Doesn't have card to defeat but other of type exists",
        #  "Does not have the card, has spade(s), must play spade",
        #   "Can play any card"]

        # index = card.get_card_index()
        len_hearts = len(player.hearts)
        len_clubs = len(player.clubs)
        len_diamonds = len(player.diamonds)
        len_spades = len(player.spades)
        # output_list = []
        card_of_type = False
        greater_card_exists = False
        if card.card_type == 'Heart' and len_hearts > 0:
            card_of_type = True
            greater_card_exists = self.greater_exists(card=card, card_list= player.hearts)
        elif card.card_type == "Club" and len_clubs > 0:
            card_of_type = True
            greater_card_exists = self.greater_exists(card=card, card_list= player.clubs)
        elif card.card_type == 'Diamond' and len_diamonds > 0:
            card_of_type = True
            greater_card_exists = self.greater_exists(card=card, card_list= player.diamonds)
        elif card.card_type == "Spade" and  len_spades > 0:
            card_of_type = True
            greater_card_exists = self.greater_exists(card=card, card_list= player.spades)
        elif card.card_type == "Spade" and len(player.spades) == 0:
            card_of_type = False
            greater_card_exists = False
            return outcome_list[-1]
        if card_of_type and greater_card_exists:
            return outcome_list[0]
        elif card_of_type and not greater_card_exists:
            return outcome_list[1]
        elif not card_of_type and not greater_card_exists and len(player.spades) > 0:
            return outcome_list[2]
        else:
            return outcome_list[-1]

    def greater_exists(self, card, card_list):
        """ Tbd"""
        card_index = card.get_card_index()
        outcome = False
        for i in card_list:
            if int(i.get_card_index()) > int(card_index):
                outcome = True
        return outcome
    

class Cards:
    """ Object of Cards. Used by Class Deck to initialize 52 cards. """
    def __init__(self, card_number, card_type, card_rank):
        self.card_number= card_number
        self.card_type = card_type
        self.card_rank = card_rank

    def __repr__(self) -> str:
        return f"Card Number:{self.card_number} Rank: {self.card_rank} Type: {self.card_type}"

    def __str__(self) -> str:
        return f"{self.card_number}: {self.card_rank} of {self.card_type}"

    def get_card_index(self):
        """ Function to get card's index"""
        return self.card_number


class DeckOfCard:
    """ tbd """
    def __init__(self):
        self.cards = []
        self.create()

    def create(self):
        """ tbd """
        card_types = ["Heart","Club","Diamond","Spade"]
        card_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]
        card_index = 1

        for card_type in card_types:
            for card_rank in card_ranks:
                self.cards.append(Cards(card_index, card_type, card_rank))
                card_index+=1

    def print_deck(self):
        """ tbd """
        for item in self.cards:
            print(f"{item}")


class Player(CardFunctions):
    """ Defind Class Player and its attributes """
    def __init__(self, player_number, full_name):
        """ tbd """
        CardFunctions.__init__(self,)
        # self.compare_winner = CardFunctions()
        self.player_number = player_number
        self.full_name = full_name
        self.cards_on_hand = [] # this stores all cards that a player possess at any given time
        self.cards_played = [] # this list stores all cards played by a player during a round       
        self.hearts = []
        self.clubs = []
        self.diamonds = []
        self.spades = []
        self.face_cards = []
        self.current_card_played = ""
        self.call_list = []
        self.eligible_cards = []
        self.win_count = 0
        self.cards_by_types()   

    def __repr__(self) -> str:
        return f"Full Name: {self.full_name}"
    
    def __str__(self) -> str:
        return f"{self.full_name}"

    def print_cards(self):
        """ tbd """
        print(f"\nPlayer {self.player_number}: {self.full_name}'s Hand")
        self.cards_on_hand.sort(key = lambda x:x.get_card_index())
        for item in self.cards_on_hand:
            print(item)

    def get_call(self):
        """ Tbd """
        try:
            self.print_cards()
            call = input("What is your call? Your call must be between 1-13.")
            if int(call) < 1 or int(call)>13:
                print("Invalid Entry!. Your call must be between 1-13.")
                self.get_call()
            else:
                self.call_list.append(int(call))
            return call
        except ValueError:
            print("Invalid Entry!. Your call must be between 1-13.")
            self.get_call()

    def print_eligible_cards(self):
        """tbd """
        print(f"\nPlayer {self.player_number}: {self.full_name}'s Eligible Cards to Play.")
        self.eligible_cards.sort(key = lambda x:x.get_card_index())
        for item in self.eligible_cards:
            print(item)    

    def get_card_list_by_type(self, card_type):
        """ tbd """
        if card_type == "Heart":
            return self.hearts
        elif card_type == "Club":
            return self.clubs
        elif card_type == "Diamond":
            return self.diamonds
        else:
            return self.spades

    def update_eligible_cards(self, play_card_dict):
        """tbd """
        player_list = list(play_card_dict)
        self.eligible_cards = []
        if len(player_list) == 0:
            self.eligible_cards = self.cards_on_hand   
        else:    
            if len(player_list) == 1:
                initial_card = play_card_dict[player_list[0]]
                initial_card_index = int(initial_card.get_card_index())
                initial_card_type = initial_card.card_type
                current_winning_card = play_card_dict[player_list[0]]
                compare_outcome_initial = self.compare_cards_by_type(self, initial_card)
            elif len(player_list) >= 2:
                initial_card = play_card_dict[player_list[0]]
                initial_card_index = int(initial_card.get_card_index())
                initial_card_type = initial_card.card_type
                current_winning_player = self.compare_winner(play_card_dict)
                current_winning_card = play_card_dict[current_winning_player]
                if initial_card == current_winning_card:
                    compare_outcome_initial = self.compare_cards_by_type(self, initial_card)
                if initial_card != current_winning_card:
                    compare_outcome_initial = self.compare_cards_by_type(self, initial_card)
                    compare_outcome_with_winner = self.compare_cards_by_type(self, play_card_dict[current_winning_player])
        
            if initial_card == current_winning_card and compare_outcome_initial == outcome_list[0]: # "Has card(s) to defeat"
                for i in self.get_card_list_by_type(initial_card_type):
                    if int(i.get_card_index()) > initial_card_index:
                        self.eligible_cards.append(i)
            elif initial_card == current_winning_card and compare_outcome_initial == outcome_list[1]: # "Doesn't have card to defeat but other of type exists"
                    self.eligible_cards = self.get_card_list_by_type(initial_card_type)
            elif initial_card == current_winning_card and compare_outcome_initial == outcome_list[2]: # "Does not have the card, has spade(s), must play spade"
                    self.eligible_cards = self.get_card_list_by_type("Spade")
            elif initial_card == current_winning_card and compare_outcome_initial ==  outcome_list[-1]: # "Can play any card"
                    self.eligible_cards = self.cards_on_hand   
            elif initial_card != current_winning_card and initial_card.card_type == current_winning_card.card_type:
                if compare_outcome_with_winner == outcome_list[0]: # "Has card(s) to defeat"
                    current_winning_card_index = int(current_winning_card.get_card_index())
                    for i in self.get_card_list_by_type(current_winning_card.card_type):
                        if int(i.get_card_index()) > current_winning_card_index:
                            self.eligible_cards.append(i)
                elif compare_outcome_with_winner  == outcome_list[1]: # "Doesn't have card to defeat but other of type exists"
                    self.eligible_cards = self.get_card_list_by_type(current_winning_card.card_type)
                elif compare_outcome_with_winner  == outcome_list[2]: # "Does not have the card, has spade(s), must play spade"
                    self.eligible_cards = self.get_card_list_by_type("Spade")
                elif compare_outcome_with_winner  ==  outcome_list[-1]: # "Can play any card"
                    self.eligible_cards = self.cards_on_hand
            elif initial_card != current_winning_card and initial_card.card_type != current_winning_card.card_type:
                if compare_outcome_initial == outcome_list[0] or compare_outcome_initial == outcome_list[1]:  # "Has card(s) to defeat" or "Doesn't have card to defeat but other of type exists"
                    self.eligible_cards = self.get_card_list_by_type(initial_card.card_type)
                elif compare_outcome_initial == outcome_list[2] or compare_outcome_initial == outcome_list[-1] and compare_outcome_with_winner == outcome_list[0]: # "Does not have the card, has spade(s), must play spade" or "Can play any card" and "Has card(s) to defeat"
                    for i in self.get_card_list_by_type("Spade"):
                        if int(i.get_card_index()) > int(current_winning_card.get_card_index()):
                            self.eligible_cards.append(i)   
                else:
                    self.eligible_cards= self.cards_on_hand         


    def get_winning_cards(self, competing_card, card_type):
        """tbd"""
    
    def sort(self):
        """ function to organize cards in order. """
        pass 

    def cards_by_types(self):
        """ Add cards to each players by specific type."""
        self.hearts = []
        self.clubs = []
        self.diamonds = []
        self.spades = []
        for x in self.cards_on_hand:
            if x.card_type == 'Heart':
                self.hearts.append(x)
            elif x.card_type == 'Club':
                self.clubs.append(x)
            elif x.card_type == 'Diamond':
                self.diamonds.append(x)
            elif x.card_type == 'Spade':
                self.spades.append(x)

    def cards_by_face_card(self):
        """ Add cards to each players by specific type."""
        self.face_cards = []
        for x in self.cards_on_hand:
            if x.card_rank == 'Ace' or x.card_rank == 'King' or  x.card_rank == 'Queen' or x.card_rank == 'Jack':
                self.face_cards.append(x)


    def get_card_index(self):
        """tbd"""
        for index, x in enumerate(self.cards_on_hand):
            if x.card_number == int(self.current_card_played):
                return index
 

    def play_card(self, play_card_dict):
        """ Function to define playing of card."""
        self.update_eligible_cards(play_card_dict)
        self.print_eligible_cards()        
        self.current_card_played = input(f"Player {self.player_number}: {self.full_name}'s Turn\nEnter the Card Number you would like to play: ")
        try:
            if (any(x.card_number == int(self.current_card_played) for x in self.eligible_cards)):
                print("Card is on Hand and eligible!")
                self.cards_played.append(self.cards_on_hand.pop(self.get_card_index()))
                self.cards_by_types()
            else:
                print("Card not on hand. Play the card available to you.")
                self.play_card(play_card_dict)
        except:
            print("Invalid Entry!")
            self.play_card(play_card_dict)
        return self.current_card_played

    def check_legal(self, play_card_dict):
        """ tbd """
        player_list = list(play_card_dict)
        card_list = list(play_card_dict.items())
        if len(card_list) == 0:
            pass
        elif len(card_list)==1:
            card_played = self.cards_on_hand[self.get_card_index()]
            first_card = play_card_dict[player_list[0]]
            first_card_card_type = first_card.card_type
            compare_first = self.compare_cards_by_type(self, first_card)
            if compare_first and first_card.card_type != card_played.card_type:
                return False
  
class Game(CardFunctions):
    """ tbd """

    def __init__(self):
        CardFunctions.__init__(self,)
        self.round_counter = 0
        self.player_one = Player(1, input("Enter Player 1 Name: ") )
        self.player_two = Player(2, input("Enter Player 2 Name: ") )
        self.player_three = Player(3, input("Enter Player 3 Name: ") )
        self.player_four = Player(4, input("Enter Player 4 Name: ") )
        self.game_deck = DeckOfCard()
        self.winners = []
        # self.play_order = []

        while self.round_counter < 5 :
            self.play_round()
            self.round_counter+=1

    def play_round(self):
        """ Function to play a round. """
        self.play_counter  = 0
        self.deal_cards()
        for player in self.play_order:
            player.get_call()
        while self.play_counter < 13:
            # play_card_list = []
            play_card_dict = {}
            while len(play_card_dict) < 4:
                for player in self.play_order:
                    player.print_cards()
                    player.play_card(play_card_dict)
                    play_card_dict.update({player: player.cards_played[-1]})
                    self.show_cards_at_play(play_card_dict)
            self.play_counter +=1
            self.evaluate_play(play_card_dict) # Evaluate here once play_card_list has 4 items. 



    def show_cards_at_play(self,play_card_dict):
        """Function to show current cards at play by players. """
        player_list = list(play_card_dict)
        print("Current Cards at Play!!")
        for item in player_list:
            print(f"\nPlayer {item} played card number {play_card_dict[item]}\n")

    def evaluate_play(self, play_card_dict):
        """ Function to evaluate an individual play. Must have 4 objects in  self.play_card_list """
        print("Evaluating winner!")
        current_winning_player = self.compare_winner(play_card_dict)


        current_winning_player.win_count+=1
        print(f"{current_winning_player} won this round!")
        self.winners.append(current_winning_player)
  
    def show_play_cards(self, play_card):
        """ Show Player's card played. """
        # print(f"Player:{}")
        pass


    def play(self):
        """ Function to define an individual play. """


    @property
    def player_list(self):
        """ Define list of player in the game"""
        return [self.player_one, self.player_two, self.player_three, self.player_four]

    @property
    def current_dealer(self):
        """ Define current_dealer in the game."""
        import random
        if self.round_counter == 0:
            self.current_dealer = random.choice(self.player_list)
        return self.current_dealer


    @property 
    def deal_order(self):
        """ Defines Deal order for the game. """
        return [self.player_two, self.player_three, self.player_four, self.player_one]
    
    @property
    def current_winner(self):
        """ Defines current winner of the game. The winner will be the dealer for next round"""
        return self.winners[-1]


    @current_winner.setter
    def current_winner(self, current_winner):
        self.current_winner = current_winner

    
    def set_play_order(self):
        """ tbd """
        if self.round_counter == 0 and self.play_counter == 0:
            return [self.player_two, self.player_three, self.player_four, self.player_one]
        elif self.winners[-1] == self.player_one:
            return [self.player_one, self.player_two, self.player_three, self.player_four]  
        elif self.winners[-1] == self.player_two:
            return [self.player_two, self.player_three, self.player_four, self.player_one] 
        elif self.winners[-1] == self.player_three:
            return [self.player_three, self.player_four, self.player_one, self.player_two]
        elif self.winners[-1] == self.player_four:
            return [self.player_four, self.player_one, self.player_two, self.player_three]    
   
    @property
    def play_order(self):
        """ Define play order based on current winner. """
        return self.set_play_order()

    # @play_order.setter
    #   def set_play_order(self):
    #     """ tbd """
    #     if self.round_counter == 0 and self.play_counter ==0:
    #         self.play_order = [self.player_two, self.player_three, self.player_four, self.player_one]
    #     elif self.winners[-1] == self.player_one:
    #         self.play_order = [self.player_one, self.player_two, self.player_three, self.player_four]  
    #     elif self.winners[-1] == self.player_two:
    #         self.play_order = [self.player_two, self.player_three, self.player_four, self.player_one] 
    #     elif self.winners[-1] == self.player_three:
    #         self.play_order = [self.player_three, self.player_four, self.player_one, self.player_two]
    #     elif self.winners[-1] == self.player_four:
    #         self.play_order = [self.player_four, self.player_one, self.player_two, self.player_three]    
    
    def update_deal_order(self):
        """ Function to update deal order based on the winner of the last round."""
        if self.round_counter == 0 and self.play_counter ==0:
            self.deal_order = [self.player_two, self.player_three, self.player_four, self.player_one]
        elif self.current_winner == self.player_one:
            self.deal_order = [self.player_two, self.player_three, self.player_four, self.player_one]
        elif self.current_winner == self.player_two:
            self.deal_order = [self.player_three, self.player_four, self.player_one, self.player_two]
        elif self.current_winner == self.player_three:
            self.deal_order = [self.player_four, self.player_one, self.player_two, self.player_three]
        elif self.current_winner == self.player_four:
            self.deal_order = [self.player_one, self.player_two, self.player_three, self.player_four]

    def deal_cards(self):
        """ Deal cards to 4 players. each players get 13 cards from the deck which must be shuffled."""
        from random import shuffle
        shuffle(self.game_deck.cards)
        i = 0
        deal_order = self.deal_order
        while i < 52:
            deal_order[0].cards_on_hand.append(self.game_deck.cards[i])
            i+=1
            deal_order[1].cards_on_hand.append(self.game_deck.cards[i])
            i+=1
            deal_order[2].cards_on_hand.append(self.game_deck.cards[i])
            i+=1
            deal_order[3].cards_on_hand.append(self.game_deck.cards[i])
            i+=1
        self.set_cards_by_types()
        deal_valid = self.check_valid_deal()
        while not deal_valid:
            self.deal_cards()
        

        # Check if the deal is valid???

    def set_cards_by_types(self):
        for i in self.deal_order:
            i.cards_by_types()
            i.cards_by_face_card()

    def check_valid_deal(self):
        output= True
        for i in self.deal_order:
            if len(i.spades)==0 or len(i.face_cards)==0:
                output = False
                break
        return output
   


    def set_deal_order(self):
        """ This function will process logic to set a deal order per round. """
        if self.round_counter== 0:
            self.deal_order = self.deal_order
            

    def scoring(self):
        """ Function to define logic for scoring. """
        pass

class GameExceptions(Exception):
    """ tbd """
    def __init__(self, message):
        super().__init__(message)


    def check_call(self,call):
        """ tbd """
        if call < 1 or call > 13:
            raise GameExceptions("Invalid entry. The entered value it outside of allowable range. The entry must be between 1-13.")

game1 = Game()


