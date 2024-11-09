require 'minitest/autorun'
require_relative './bt'
class BTreeLettersTest < Minitest::Test
  def test_bt
    @tree = BTreeLetters.new(2)
    @tree.print
  end
end