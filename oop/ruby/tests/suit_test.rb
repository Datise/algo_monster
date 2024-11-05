require "minitest/autorun"
require_relative "../playing_cards"

class TestSuit < Minitest::Test
  def setup
    @suit = Suit.new("hearts")
  end

  def test_to_s
    assert_equal "hearts", @suit.to_s
  end

  def test_raises_error_with_invalid_arg
    @error = assert_raises ArgumentError do
      Suit.new("fish")
    end
  end
end