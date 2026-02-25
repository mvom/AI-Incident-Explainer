describe('AI Incident Chat E2E', () => {
  it('should display initial AI message and send/receive messages', () => {
    cy.visit('/');
    cy.contains('Ask me anything').should('exist');
    cy.get('input[placeholder="Type your question..."]').type('How many turbines?');
    cy.contains('Send').click();
    cy.contains('Typing...').should('exist');
    cy.contains('turbine').should('exist'); // Will match if backend responds
  });
});
