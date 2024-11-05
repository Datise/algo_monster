require "minitest/autorun"
require_relative "../playing_cards"

class TestCard < Minitest::Test
  def setup
    @card = Card.new("hearts", "Q")
  end

  def test_to_s
    assert_equal "Q of hearts", @card.to_s
  end

  def test_value
    assert_equal 12, @card.value
  end

  def test_raises_error_with_invalid_suit
    assert_raises ArgumentError do
      Card.new("fish")
    end
  end

  def test_raises_error_with_invalid_val
    assert_raises ArgumentError do
      Card.new("hearts", "KA")
    end
  end

  def test_raises_error_with_invalid_int
    assert_raises ArgumentError do
      Card.new("hearts", 15)
    end
  end
end