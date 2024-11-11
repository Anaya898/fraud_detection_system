@Entity
public class Customer {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int customerId;
    private String name;
    private String email;
    private String phone;
    private Timestamp createdAt;

    // Getters and setters
}
