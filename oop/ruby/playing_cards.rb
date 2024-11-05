class Suit 
	TYPES = [ "hearts", "diamonds", "spades", "clubs"]
	def initialize(type)
		if !TYPES.include?(type)
			raise ArgumentError.new "#{type} not in #{TYPES}"
		end
		@type = type
	end

	def to_s
		@type
	end
	
	def self.TYPES
		TYPES
	end
end

class Card

	@@values = {"A" => 1, "J" => 11, "Q" => 12, "K" => 13, "Joker" => 14}
	9.times do |x| 
		val = x + 2 
		@@values[val] = val
	end

	def initialize(suit, value)
		@suit = Suit.new(suit)
		if !@@values.has_key?(value)
			raise ArgumentError.new "Invalid value, please use #{@@values.keys}"
		end
		@value = value
	end

	def to_s
		"#{@value} of #{@suit}"
	end

	def value
		@@values[@value]
	end

	def self.values
		@@values
	end
end

class JokerSuit < Suit
	TYPES = ["black", "red"]
	def initialize(suit)
		super(suit)
	end
end

class Joker < Card
	
	def initialize(suit)
		@suit = JokerSuit.new(suit)
		@value = "Joker"
	end
end

class Hand
	attr_accessor :cards
	def initialize
		@cards = []
	end

	def to_s
		@cards.each(&:to_s)
	end
end

class Game
	def initialize
		@cards = []
		@hands = []
	end

	def add_card(suit, value)
		@cards.push(Card.new(suit, value))
	end

	def add_joker(color)
		@cards.push(Joker.new(color))
	end

	def card_string(position)
		@cards[position].to_s
	end

	def add_hand()
		hand = Hand.new
		@hands.push(hand)
		5.times do |x|
			card = Card.new(Suit.TYPES.sample, Card.values.keys.sample)
			@cards.push(card)
			hand.cards.push(card)
		end
	end

	def hand_string(hand)
		@hands[hand].to_s
	end

	def card_beats(a, b)
		@cards[a].value > @cards[b].value
	end
end


# game = Game.new
# game.add_card("hearts", "Q")
# game.add_card("spades", "K")
# game.add_hand
# puts game.hand_string(0)
