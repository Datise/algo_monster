require "minitest/autorun"
require_relative "../playing_cards"

class TestCard < Minitest::Test

  def setup
    @game = Game.new
  end
end