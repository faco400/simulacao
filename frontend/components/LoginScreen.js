import React from 'react';
import { StyleSheet, View, TextInput, Button } from 'react-native';

const LoginScreen = ({ navigation }) => {
  const handleLogin = () => {
 
    alert('Login realizado!');
  };

  const goToSignUp = () => {
    navigation.navigate('Cadastro');
  };

  return (
    <View style={styles.container}>
      <TextInput
        placeholder="Email"
        style={styles.input}
        placeholderTextColor="#777"
      />
      <TextInput
        placeholder="Senha"
        style={styles.input}
        secureTextEntry
        placeholderTextColor="#777"
      />
      <Button title="Entrar" onPress={handleLogin} style={styles.button} />
      <View style={styles.signupContainer}>
        <Button
          title="Registrar"
          onPress={goToSignUp}
          style={[styles.button, styles.signupButton]}
        />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    padding: 15,
    backgroundColor: '#fff', 
  },
  input: {
    marginBottom: 40,
    backgroundColor: '#f0f0f0', 
    paddingHorizontal: 10,
    paddingVertical: 8,
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 5,
    fontSize: 16,
    color: '#333',
  },
  button: {
    paddingVertical: 12,
    backgroundColor: '#007bff', 
    borderRadius: 5,
    marginBottom: 10, 
  },
  
  signupContainer: {
    marginTop: 30,
  },
  signupButton: {
    backgroundColor: '#28a745', 
  },
});

export default LoginScreen;
