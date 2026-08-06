import { View, Text, TouchableOpacity, StyleSheet } from "react-native";

export default function Dashboard() {
  return (
    <View style={styles.container}>
      {/* Header */}
      <Text style={styles.greeting}>Welcome Back 👋</Text>
      <Text style={styles.username}>Sethmindu</Text>

      {/* Balance Card */}
      <View style={styles.balanceCard}>
        <Text style={styles.balanceTitle}>Total Savings</Text>
        <Text style={styles.balanceAmount}>LKR 40,000</Text>
      </View>

      {/* Stats */}
      <View style={styles.row}>
        <View style={styles.smallCard}>
          <Text style={styles.cardTitle}>👥 Circle</Text>
          <Text style={styles.cardValue}>4 Members</Text>
        </View>

        <View style={styles.smallCard}>
          <Text style={styles.cardTitle}>📅 Round</Text>
          <Text style={styles.cardValue}>Round 1</Text>
        </View>
      </View>

      {/* Quick Actions */}
      <Text style={styles.sectionTitle}>Quick Actions</Text>

      <TouchableOpacity style={styles.button}>
        <Text style={styles.buttonText}>➕ Create Circle</Text>
      </TouchableOpacity>

      <TouchableOpacity style={styles.button}>
        <Text style={styles.buttonText}>🤝 Join Circle</Text>
      </TouchableOpacity>

      <TouchableOpacity style={styles.button}>
        <Text style={styles.buttonText}>💵 Contribute</Text>
      </TouchableOpacity>

      <TouchableOpacity style={[styles.button, styles.logout]}>
        <Text style={styles.buttonText}>🚪 Logout</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#F4F7FB",
    padding: 25,
    paddingTop: 60,
  },

  greeting: {
    fontSize: 18,
    color: "#666",
  },

  username: {
    fontSize: 32,
    fontWeight: "bold",
    marginBottom: 25,
    color: "#222",
  },

  balanceCard: {
    backgroundColor: "#2563EB",
    borderRadius: 18,
    padding: 25,
    marginBottom: 25,
  },

  balanceTitle: {
    color: "#DCE7FF",
    fontSize: 16,
  },

  balanceAmount: {
    color: "white",
    fontSize: 34,
    fontWeight: "bold",
    marginTop: 8,
  },

  row: {
    flexDirection: "row",
    justifyContent: "space-between",
    marginBottom: 30,
  },

  smallCard: {
    backgroundColor: "white",
    width: "48%",
    borderRadius: 15,
    padding: 20,
    elevation: 4,
  },

  cardTitle: {
    color: "#666",
    fontSize: 15,
  },

  cardValue: {
    marginTop: 10,
    fontSize: 20,
    fontWeight: "bold",
    color: "#111",
  },

  sectionTitle: {
    fontSize: 22,
    fontWeight: "bold",
    marginBottom: 18,
    color: "#222",
  },

  button: {
    backgroundColor: "#2563EB",
    padding: 16,
    borderRadius: 12,
    marginBottom: 15,
  },

  logout: {
    backgroundColor: "#EF4444",
    marginTop: 15,
  },

  buttonText: {
    color: "white",
    textAlign: "center",
    fontSize: 17,
    fontWeight: "bold",
  },
});