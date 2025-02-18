/**
 * Purpose: Used to test the implementation of Player and Monster classes
 *
 * @author ITSC 1213
 * @version Feb 01, 2025
 */
public class Playground {

    public static void main(String[] args) {
        // Create a Player object
        Player player = new Player(100, 50, 0);

        // Display initial player status
        player.displayStatus();

        // Player gains XP and heals
        player.gainXp(20);
        player.heal(10);
        // Display updated player status
        player.displayStatus();

        // Create Monster objects
        Monster dragon = new Monster("Dragon", 150);
        Monster goblin = new Monster("Goblin", 50);

        // Display monster status
        dragon.displayStatus();
        goblin.displayStatus();

        // Monsters take damage
        dragon.takeDamage(30);
        goblin.takeDamage(10);

        // Display updated monster status
        dragon.displayStatus();
        goblin.displayStatus();

        // Monster roars at player
        dragon.roar(player);
        // Display updated monster status
        player.displayStatus();
    }
}
