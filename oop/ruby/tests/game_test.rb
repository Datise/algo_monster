require "minitest/autorun"
require_relative "../playing_cards"

class TestCard < Minitest::Test

  def setup
    @game = Game.new
  end

  def test_add_card
    @game.add_card("diamonds", "7")
    assert_contains @game.cards, "7 of diamonds"
    assert_equal "7 of diamonds", @game.card_string(0)
  end
end