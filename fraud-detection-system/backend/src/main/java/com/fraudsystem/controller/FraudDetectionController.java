package com.fraudsystem.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import com.fraudsystem.model.Transaction;
import com.fraudsystem.service.TransactionService;

@RestController
@RequestMapping("/api/transactions")
public class FraudDetectionController {
    @Autowired
    private TransactionService transactionService;

    @PostMapping("/analyze")
    public Transaction analyzeTransaction(@RequestBody Transaction transaction) {
        return transactionService.analyzeTransaction(transaction);
    }
}
