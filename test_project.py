import pytest
from project import display_intro, get_player_choice, process_choice

@pytest.fixture
def setup_game():
    return []  

def test_display_intro(capsys):
    display_intro()
    captured = capsys.readouterr()
    assert "It's prom night! You're feeling a little nervous" in captured.out
    assert "You bump into someone! It's..." in captured.out 
    assert "1. The popular football captain" in captured.out
    assert "2. The quiet guy" in captured.out
    assert "3. The funny guy" in captured.out
    assert "4. Quit" in captured.out 

def test_get_player_choice_valid():
    with patch('builtins.input', return_value='1'):
        assert get_player_choice() == '1'

def test_get_player_choice_invalid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '5')
    with pytest.raises(ValueError):
        get_player_choice()

def test_process_choice_quit(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'quit')
    with patch('sys.exit') as mock_exit: 
        process_choice('quit', [])
    mock_exit.assert_called_once()  

def test_process_choice_football_captain_dance_yes(setup_game):  
    with patch('builtins.input', side_effect=['yes']):
        process_choice('1', setup_game)
 

def test_process_choice_football_captain_dance_no(setup_game, capsys):
    with patch('builtins.input', side_effect=['no']):
        process_choice('1', setup_game)
    captured = capsys.readouterr()
    assert "You decline politely" in captured.out 

def test_process_choice_quiet_guy_talk_yes(setup_game, capsys):
    with patch('builtins.input', side_effect=['yes']):
        process_choice('2', setup_game)
    captured = capsys.readouterr()
    assert "You have a nice conversation" in captured.out

def test_process_choice_quiet_guy_talk_no(setup_game, capsys): 
    with patch('builtins.input', side_effect=['no']):
        process_choice('2', setup_game)
    captured = capsys.readouterr()
    assert "You decide to talk to someone else" in captured.out 

def test_process_choice_quiet_guy_dance_yes(setup_game):  
    with patch('builtins.input', side_effect=['yes', 'yes']):
        process_choice('2', setup_game) 
    assert 'kiss' in setup_game

def test_process_choice_quiet_guy_dance_no(setup_game, capsys):
    with patch('builtins.input', side_effect=['yes', 'no']):
        process_choice('2', setup_game)
    captured = capsys.readouterr()
    assert "You decline politely" in captured.out 

def test_process_choice_funny_guy_laugh_yes(setup_game, capsys):
    with patch('builtins.input', side_effect=['yes']):
        process_choice('3', setup_game)
    captured = capsys.readouterr()
    assert "You have a great time laughing" in captured.out

def test_process_choice_funny_guy_laugh_no(setup_game, capsys):
    with patch('builtins.input', side_effect=['no']):
        process_choice('3', setup_game)
    captured = capsys.readouterr()
    assert "You're not in the mood" in captured.out 

def test_process_choice_funny_guy_dance_yes(setup_game):
    with patch('builtins.input', side_effect=['yes', 'yes']):
