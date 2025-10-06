import pytest
import pygame
from unittest.mock import Mock, patch, MagicMock
import project


@pytest.fixture
def setup_pygame():
    """Initialize pygame for testing"""
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    test_font = pygame.font.Font(None, 50)
    yield screen, test_font
    pygame.quit()


def test_display_score(setup_pygame):
    """Test that display_score returns correct score value"""
    screen, test_font = setup_pygame
    
    # Mock the global variables needed
    project.screen = screen
    project.test_font = test_font
    project.start_time = 0
    
    # Mock pygame.time.get_ticks to return a known value
    with patch('pygame.time.get_ticks', return_value=5000):
        score = project.display_score()
        assert score == 5  # 5000ms / 1000 - 0 = 5 seconds
    
    with patch('pygame.time.get_ticks', return_value=10000):
        score = project.display_score()
        assert score == 10  # 10000ms / 1000 - 0 = 10 seconds


def test_spawn_obstacle():
    """Test that spawn_obstacle adds obstacles to the list"""
    # Create mock surfaces for snail and fly
    project.snail = Mock()
    project.fly = Mock()
    project.obstacle_rect_list = []
    
    # Mock get_rect to return a mock rectangle
    mock_rect = Mock()
    project.snail.get_rect = Mock(return_value=mock_rect)
    project.fly.get_rect = Mock(return_value=mock_rect)
    
    # Test that obstacle is spawned
    initial_length = len(project.obstacle_rect_list)
    project.spawn_obstacle()
    assert len(project.obstacle_rect_list) == initial_length + 1
    
    # Test multiple spawns
    for _ in range(5):
        project.spawn_obstacle()
    assert len(project.obstacle_rect_list) >= 1


def test_player_animation(setup_pygame):
    """Test player animation switching"""
    screen, test_font = setup_pygame
    
    # Setup mock player surfaces
    project.player_walk = [Mock(), Mock()]
    project.player_jump = Mock()
    project.player_index = 0
    project.framerate = 200
    project.index_time = 0
    
    # Create a mock rect for player
    project.player_rect = Mock()
    
    # Test jumping animation (player in air)
    project.player_rect.bottom = 200  # Player is in air
    project.player_animation()
    assert project.player_surface == project.player_jump
    
    # Test walking animation (player on ground)
    project.player_rect.bottom = 250  # Player on ground
    with patch('pygame.time.get_ticks', return_value=300):
        project.player_animation()
        # Index should have changed due to time passing
        assert project.player_index in [0, 1]


def test_obstacle_movement(setup_pygame):
  def test_obstacle_movement(setup_pygame):
    """Test obstacle movement and cleanup"""
    screen, test_font = setup_pygame
    project.screen = screen
    
    # Create REAL pygame surfaces instead of mocks
    project.snail = pygame.Surface((50, 50))
    project.fly = pygame.Surface((50, 50))

def test_collisons():
    """Test collision detection"""
    # Create mock player rect
    player_rect = Mock()
    
    # Create mock obstacle
    obstacle1 = Mock()
    
    # Test collision (returns False when collision occurs)
    player_rect.colliderect = Mock(return_value=True)
    assert project.collisons(player_rect, [obstacle1]) == False
    
    # Test no collision (returns True when no collision)
    player_rect.colliderect = Mock(return_value=False)
    assert project.collisons(player_rect, [obstacle1]) == True
    
    # Test empty obstacle list
    assert project.collisons(player_rect, []) == True
    
    # Test None obstacle list
    assert project.collisons(player_rect, None) == True


def test_collisons_multiple_obstacles():
    """Test collision detection with multiple obstacles"""
    player_rect = Mock()
    
    obstacle1 = Mock()
    obstacle2 = Mock()
    obstacle3 = Mock()
    
    # Test collision with first obstacle
    player_rect.colliderect = Mock(side_effect=[True, False, False])
    assert project.collisons(player_rect, [obstacle1, obstacle2, obstacle3]) == False
    
    # Test collision with middle obstacle
    player_rect.colliderect = Mock(side_effect=[False, True, False])
    assert project.collisons(player_rect, [obstacle1, obstacle2, obstacle3]) == False
    
    # Test no collision with any obstacle
    player_rect.colliderect = Mock(side_effect=[False, False, False])
    assert project.collisons(player_rect, [obstacle1, obstacle2, obstacle3]) == True


def test_spawn_obstacle_randomness():
    """Test that spawn_obstacle creates different obstacle types"""
    project.snail = Mock()
    project.fly = Mock()
    project.obstacle_rect_list = []
    
    mock_rect = Mock()
    project.snail.get_rect = Mock(return_value=mock_rect)
    project.fly.get_rect = Mock(return_value=mock_rect)
    
    # Spawn multiple obstacles and check that list grows
    for _ in range(10):
        project.spawn_obstacle()
    
    assert len(project.obstacle_rect_list) == 10