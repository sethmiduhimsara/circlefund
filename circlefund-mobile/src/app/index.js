import { useState } from "react";
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  Alert,
  StyleSheet,
} from "react-native";
import { router } from "expo-router";
import api from "../services/api";

export default function LoginScreen() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const login = async () => {
    try {
      const response = await api.post("login/", {
        username,
        password,
      });

      console.log(response.data);

      Alert.alert("Success", "Login Successful!");

      router.push("/dashboard");
    } catch (error) {
      console.log(error.response?.data);
      Alert.alert("Login Failed", "Invalid username or password");
    }
  };

  return (
    <View style={styles.container}>
      <View style={styles.card}>
        <Text style={styles.logo}>💰</Text>

        <Text style={styles.title}>CircleFund</Text>

        <Text style={styles.subtitle}>
          Welcome back! Sign in to continue.
        </Text>

        <TextInput
          placeholder="Username"
          placeholderTextColor="#888"
          value={username}
          onChangeText={setUsername}
          style={styles.input}
        />

        <TextInput
          placeholder="Password"
          placeholderTextColor="#888"
          secureTextEntry
          value={password}
          onChangeText={setPassword}
          style={styles.input}
        />

        <TouchableOpacity style={styles.button} onPress={login}>
          <Text style={styles.buttonText}>Login</Text>
        </TouchableOpacity>

        <Text style={styles.footer}>
          Circle Savings Platform
        </Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#EEF3F8",
    justifyContent: "center",
    alignItems: "center",
    padding: 20,
  },

  card: {
    width: "100%",
    maxWidth: 380,
    backgroundColor: "#FFFFFF",
    padding: 30,
    borderRadius: 20,
    shadowColor: "#000",
    shadowOffset: {
      width: 0,
      height: 10,
    },
    shadowOpacity: 0.15,
    shadowRadius: 15,
    elevation: 8,
  },

  logo: {
    fontSize: 60,
    textAlign: "center",
    marginBottom: 15,
  },

  title: {
    fontSize: 30,
    fontWeight: "bold",
    color: "#1F2937",
    textAlign: "center",
  },

  subtitle: {
    textAlign: "center",
    color: "#6B7280",
    marginTop: 8,
    marginBottom: 30,
    fontSize: 15,
  },

  input: {
    backgroundColor: "#F5F7FA",
    borderRadius: 12,
    padding: 15,
    marginBottom: 16,
    fontSize: 16,
    borderWidth: 1,
    borderColor: "#E5E7EB",
  },

  button: {
    backgroundColor: "#2563EB",
    padding: 16,
    borderRadius: 12,
    marginTop: 10,
  },

  buttonText: {
    color: "#FFFFFF",
    textAlign: "center",
    fontWeight: "bold",
    fontSize: 17,
  },

  footer: {
    textAlign: "center",
    marginTop: 24,
    color: "#9CA3AF",
    fontSize: 13,
  },
});