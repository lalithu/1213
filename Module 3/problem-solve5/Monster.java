/**
 * Purpose: Represents a monster with health and a name. The monster can take damage, regain health, roar, and display its current status.
 * 
 * @author  ITSC 1213
 * @version Feb 01, 2025
 */
public class Monster {
    
    private String naam = "Barfi";
    private int health;

    // Method Signature: takeDamage(int dmg) -> void
    // Purpose: Reduces the monster's health by the specified amount, ensuring health
    // does not drop below 0.
    // Example: m.takeDamage(30) --> Monster health decreases by 30 (e.g., 100 to 70)
    // To-Do: Add takeDamage method

    public void takeDamage(int dmg) {        
        if ((health - dmg) >= 0) {
            health = health - dmg; // health -=dmg
        }
    }

    // Method Signature: heal(int amount) -> void
    // Purpose: Increases the monster's health by the specified amount, ensuring it
    // does not exceed a maximum value.
    // Example: m.heal(20) --> Monster health increases by 20 (e.g., 70 to 90)
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
    // Purpose: Prints the monster's current health, gold, and experience points.
    // Example: m.displayStatus() --> Outputs current stats of the monster
    // To-Do: Add displayStatus method

    public void displayStatus() {
        // System.out.println("Health: " + health);
        // System.out.println("Gold: " + gold);
        //System.out.println("Experience points: " + Xp);

        System.out.println("Health: " + health + "\tGold: " + gold + "\tExperience points " + Xp);
    }
}
