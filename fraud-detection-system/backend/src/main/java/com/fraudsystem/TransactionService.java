package main.java.com.fraudsystem;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.fraudsystem.model.Transaction;
import com.fraudsystem.repository.TransactionRepository;
import org.springframework.web.client.RestTemplate;

@Service
public class TransactionService {
    @Autowired
    private TransactionRepository transactionRepository;

    private final String ML_API_URL = "http://flask-api:5000/predict";

    public Transaction analyzeTransaction(Transaction transaction) {
        RestTemplate restTemplate = new RestTemplate();
        String prediction = restTemplate.postForObject(ML_API_URL, transaction, String.class);
        transaction.setStatus(prediction.equals("fraud") ? "FRAUD" : "LEGIT");
        return transactionRepository.save(transaction);
    }
}
