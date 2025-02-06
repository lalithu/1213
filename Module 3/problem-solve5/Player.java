/**
 * Purpose: Represents a player in the game with health, gold, and experience points.
 *
 * @author  ITSC 1213
 * @version Feb 01, 2025
 */
public class Player {
    /*
     * ****************
     * Data Definitions
     * ****************
     * Attributes: health (int), gold (int), and experience points (int)
     * - health (int): Represents the player's current health points.
     * - gold (int): Represents the player's current gold points (currency they can
     * use in the game).
     * - xp (int): Represents the player's current experience points (tracks overall
     * progression / level in the game).
     */

     private int health; // Health
     private int gold; // Gold
     private int Xp; // Experience points

    // Constructor Signature:Player(int startHealth, int startGold, int startXP)
    // Example: Player(100, 50, 0) --> Initialzes a Player object with health set to 100, gold set to 50 and xp set to 0
    // To-Do: Add constructor and initialize attributes

    public Player(int startHealth, int startGold, int startXP) {
        health = startHealth;
        gold = startGold;
        Xp = startXP;
    }

    // Method Signature: gainXp(int amount) -> void
    // Purpose: Increases the player's experience points by the specified amount
    // Example: p.gainXp(20) --> Player xp increases by 20 
    // To-Do: Add gainXp method

    public void gainXp(int amount) {
        Xp = Xp + amount;
    }

    // Method Signature: takeDamage(int dmg) -> void
    // Purpose: Reduces the player's health by the specified amount, ensuring health
    // does not drop below 0.
    // Example: p.takeDamage(30) --> Player health decreases by 30 (e.g., 100 to 70)
    // To-Do: Add takeDamage method

    public void takeDamage(int dmg) {        
        if ((health - dmg) >= 0) {
            health = health - dmg; // health -=dmg
        }
    }

    // Method Signature: heal(int amount) -> void
    // Purpose: Increases the player's health by the specified amount, ensuring it
    // does not exceed a maximum value.
    // Example: p.heal(20) --> Player health increases by 20 (e.g., 70 to 90)
    // To-Do: Add heal method

    public void heal(int amount) {     
        int maxHealth = 25;

        if (amount > maxHealth) {
            health += maxHealth;
        } else {
            health += amount;
        }
    }

    // Method Signature: displayStatus() -> void
    // Purpose: Prints the player's current health, gold, and experience points.
    // Example: p.displayStatus() --> Outputs current stats of the player
    // To-Do: Add displayStatus method

    public void displayStatus() {
        // System.out.println("Health: " + health);
        // System.out.println("Gold: " + gold);
        //System.out.println("Experience points: " + Xp);

        System.out.println("Health: " + health + "\tGold: " + gold + "\tExperience points " + Xp);
    }
}
